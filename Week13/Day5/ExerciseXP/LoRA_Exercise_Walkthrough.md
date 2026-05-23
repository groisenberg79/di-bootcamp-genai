# LoRA Exercise Walkthrough

This file explains the notebook `Exercises_XP_Week13_Day5_LoRA.ipynb` step by step and fills in the missing `TODO` values.

## 1. Big picture: what LoRA is

LoRA means **Low-Rank Adaptation**.

Instead of training a whole weight matrix `W`, we:

- keep the original weight matrix frozen
- add a small trainable correction
- make that correction low-rank so it uses far fewer parameters

For a linear layer, normal output is:

```python
y = x @ W.T + b
```

LoRA changes this idea to:

```python
y = x @ W.T + alpha * (x @ A @ B) + b
```

Where:

- `W` is the original pretrained weight
- `A` has shape `(in_dim, rank)`
- `B` has shape `(rank, out_dim)`
- `A @ B` approximates a full update matrix of shape `(in_dim, out_dim)`
- `rank` is small, so training is cheaper

If `rank` is much smaller than `in_dim` and `out_dim`, then the number of trainable parameters is much smaller than training a full dense matrix.

## 2. What each package is doing

### `torch`

This is the main PyTorch package. It gives us tensors, random initialization, device handling, and math operations.

Examples in the notebook:

- `torch.randn(...)`
- `torch.manual_seed(...)`
- `torch.device(...)`

### `torch.nn as nn`

This contains neural-network building blocks.

Examples:

- `nn.Module` for defining our own layers
- `nn.Linear` for standard dense layers
- `nn.Parameter` for tensors that should be trained
- `nn.Sequential` for stacking layers
- `nn.ReLU` for activation functions

### `torch.nn.functional as F`

This contains stateless neural-network functions.

Examples:

- `F.linear(...)` applies a linear layer manually
- `F.cross_entropy(...)` computes classification loss

Use `nn.Linear` when you want a reusable layer with stored weights.
Use `F.linear` when you already have weights and just want to apply the operation directly.

### `torch.utils.data.DataLoader`

This makes it easy to loop over a dataset in mini-batches.

It handles:

- batching
- shuffling
- iteration

### `torchvision.datasets`

This gives ready-to-use vision datasets, including MNIST.

### `torchvision.transforms`

This converts raw images into tensors and can apply preprocessing.

In this notebook, `transforms.ToTensor()` converts images to PyTorch tensors.

### `copy`

This is Python's standard library module for copying objects.

`copy.deepcopy(model)` creates a fully separate copy of the trained MLP before replacing layers with LoRA versions.

### `time`

Used only to measure training time.

## 3. Exercise 1: Implement `LoRALayer`

### Goal

Build the low-rank update itself.

### Why the shapes work

If:

- `x` is `(batch, in_dim)`
- `A` is `(in_dim, rank)`
- `B` is `(rank, out_dim)`

Then:

- `x @ A` becomes `(batch, rank)`
- `(x @ A) @ B` becomes `(batch, out_dim)`

That gives a valid output for the adapter.

### Why `B` starts at zero

This is very important.

If `B` starts at zero, then:

```python
x @ A @ B = 0
```

So at the beginning, the LoRA path contributes nothing. That means the wrapped layer behaves exactly like the original base model before fine-tuning starts.

### Fill-in code

```python
class LoRALayer(nn.Module):
    def __init__(self, in_dim, out_dim, rank, alpha):
        super().__init__()
        std_dev = 1 / torch.sqrt(torch.tensor(rank).float())
        self.A = nn.Parameter(torch.randn(in_dim, rank) * std_dev)
        self.B = nn.Parameter(torch.zeros(rank, out_dim))
        self.alpha = alpha

    def forward(self, x):
        x = self.alpha * (x @ self.A @ self.B)
        return x

# Hyperparameters for the sandbox test
random_seed = 123
in_dim = 5
out_dim = 3
rank = 2
alpha = 1

torch.manual_seed(random_seed)
layer = LoRALayer(in_dim, out_dim, rank, alpha)
x = torch.randn(4, in_dim)

print(x)
print(layer)
print("Original output:", layer(x))
```

### What to notice

- `A` is random
- `B` is zero
- so the output will start as all zeros

That is expected and correct.

## 4. Exercise 2: Wrap `nn.Linear` with LoRA

### Goal

Keep the original linear layer and add the LoRA update on top.

The idea is:

```python
output = base_linear(x) + lora_update(x)
```

### Fill-in code

```python
class LinearWithLoRA(nn.Module):
    def __init__(self, linear, rank, alpha):
        super().__init__()
        self.linear = linear
        self.lora = LoRALayer(
            linear.in_features,
            linear.out_features,
            rank,
            alpha,
        )

    def forward(self, x):
        return self.linear(x) + self.lora(x)

base_linear = nn.Linear(in_dim, out_dim)
layer_lora_1 = LinearWithLoRA(base_linear, rank=rank, alpha=alpha)
print("LinearWithLoRA output:", layer_lora_1(x))
```

### Why this works

- `self.linear(x)` is the original model behavior
- `self.lora(x)` is the trainable correction
- adding them produces a LoRA-enhanced layer

At initialization, `self.lora(x)` is zero, so the output matches the original linear layer.

## 5. Exercise 3: Replace one network layer with LoRA

### Goal

Show that swapping a normal `nn.Linear` layer with a LoRA wrapper does not change the output at the start.

### Fill-in code

```python
class SingleLayerNet(nn.Module):
    def __init__(self, num_features, num_classes):
        super().__init__()
        self.layer = nn.Linear(num_features, num_classes)

    def forward(self, x):
        return self.layer(x)

single_net = SingleLayerNet(num_features=in_dim, num_classes=out_dim)
sample_input = torch.randn(2, in_dim)

with torch.no_grad():
    baseline_output = single_net(sample_input)

single_net.layer = LinearWithLoRA(single_net.layer, rank=rank, alpha=alpha)

with torch.no_grad():
    lora_output = single_net(sample_input)

print("Outputs match before training?", torch.allclose(baseline_output, lora_output))
```

### Why the outputs match

Because `B` is initialized to zeros.

That makes the LoRA update zero, so:

```python
wrapped_output = original_output + 0
```

This is one of the main practical benefits of LoRA: you can attach adapters to a pretrained model without disturbing its starting behavior.

## 6. Exercise 4: Merged-weight LoRA

### Goal

Express LoRA as a modified weight matrix instead of two separate forward paths.

We know:

```python
self.linear(x) + self.lora(x)
```

means:

```python
x @ W.T + alpha * (x @ A @ B) + b
```

This can be rewritten as:

```python
x @ (W + alpha * (A @ B).T).T + b
```

### Important shape detail

- `self.linear.weight` has shape `(out_dim, in_dim)`
- `A @ B` has shape `(in_dim, out_dim)`

So you must transpose `A @ B` before adding it to the original weight.

### Fill-in code

```python
class LinearWithLoRAMerged(nn.Module):
    def __init__(self, linear, rank, alpha):
        super().__init__()
        self.linear = linear
        self.lora = LoRALayer(
            linear.in_features,
            linear.out_features,
            rank,
            alpha,
        )

    def forward(self, x):
        lora = self.lora.A @ self.lora.B
        combined_weight = self.linear.weight + self.lora.alpha * lora.T
        return F.linear(x, combined_weight, self.linear.bias)

layer_lora_2 = LinearWithLoRAMerged(base_linear, rank=rank, alpha=alpha)
print("Merged LoRA output:", layer_lora_2(x))
```

### One subtle note

If you create `layer_lora_1` and `layer_lora_2` separately, they will not literally share the same `A` and `B`.

But at initialization they still behave the same because `B` starts at zero. If you wanted exact equality after training, you would need to copy the LoRA weights from one module into the other.

## 7. Exercise 5: Build the MLP

### Goal

Create a 3-layer classifier for MNIST.

MNIST images are `28 x 28`, so when flattened they become `784` features.

### Fill-in code

```python
class MultilayerPerceptron(nn.Module):
    def __init__(self, num_features, num_hidden_1, num_hidden_2, num_classes):
        super().__init__()
        self.layers = nn.Sequential(
            nn.Linear(num_features, num_hidden_1),
            nn.ReLU(),
            nn.Linear(num_hidden_1, num_hidden_2),
            nn.ReLU(),
            nn.Linear(num_hidden_2, num_classes),
        )

    def forward(self, x):
        x = self.layers(x)
        return x
```

```python
# Architecture
num_features = 28 * 28
num_hidden_1 = 256
num_hidden_2 = 128
num_classes = 10

# Settings
DEVICE = torch.device('cuda' if torch.cuda.is_available() else 'cpu')
learning_rate = 0.001
num_epochs = 3

model = MultilayerPerceptron(
    num_features=num_features,
    num_hidden_1=num_hidden_1,
    num_hidden_2=num_hidden_2,
    num_classes=num_classes,
)

model.to(DEVICE)
optimizer_pretrained = torch.optim.Adam(model.parameters(), lr=learning_rate)
print(DEVICE)
print(model)
print(optimizer_pretrained)
```

### Why these values

- `28 * 28` because MNIST images are flattened
- `10` classes because digits go from `0` to `9`
- `256` and `128` are reasonable hidden sizes for a small MLP
- `Adam` is an easy optimizer choice for this kind of exercise

## 8. Load MNIST

### Fill-in code

```python
BATCH_SIZE = 64

train_dataset = datasets.MNIST(root='data', train=True, transform=transforms.ToTensor(), download=True)

test_dataset = datasets.MNIST(root='data', train=False, transform=transforms.ToTensor(), download=True)

train_loader = DataLoader(train_dataset, batch_size=BATCH_SIZE, shuffle=True)

test_loader = DataLoader(test_dataset, batch_size=BATCH_SIZE, shuffle=False)

for images, labels in train_loader:
    print('Image batch dimensions:', images.shape)
    print('Image label dimensions:', labels.shape)
    break
```

### What the shapes mean

For MNIST, a batch of images usually has shape:

```python
(batch_size, 1, 28, 28)
```

That means:

- batch dimension
- 1 channel because the image is grayscale
- height 28
- width 28

The model expects flat vectors, so later we reshape to `(batch_size, 784)`.

## 9. Accuracy function

### Goal

Measure how many predictions are correct.

### Fill-in code

```python
def compute_accuracy(model, data_loader, device):
    model.eval()
    correct_pred, num_examples = 0, 0
    with torch.no_grad():
        for features, targets in data_loader:
            features = features.view(features.size(0), -1).to(device)
            targets = targets.to(device)
            logits = model(features)
            _, predicted_labels = torch.max(logits, 1)
            num_examples += targets.size(0)
            correct_pred += (predicted_labels == targets).sum().item()
    return (correct_pred / num_examples) * 100
```

### Why `view(features.size(0), -1)` is used

The images come in as `(batch, 1, 28, 28)`.

We flatten them into:

```python
(batch, 784)
```

because `nn.Linear` expects a 2D tensor shaped like:

```python
(batch, num_features)
```

## 10. Training loop

### Fill-in code

```python
def train(num_epochs, model, optimizer, train_loader, device):
    start_time = time.time()
    for epoch in range(num_epochs):
        model.train()
        for batch_idx, (features, targets) in enumerate(train_loader):
            features = features.view(features.size(0), -1).to(device)
            targets = targets.to(device)

            logits = model(features)
            loss = F.cross_entropy(logits, targets)
            optimizer.zero_grad()

            loss.backward()

            optimizer.step()

            if not batch_idx % 400:
                print('Epoch: %03d/%03d|Batch %03d/%03d| Loss: %.4f' % (epoch+1, num_epochs, batch_idx, len(train_loader), loss))

        with torch.set_grad_enabled(False):
            print('Epoch: %03d/%03d training accuracy: %.2f%%' % (epoch+1, num_epochs, compute_accuracy(model, train_loader, device)))

        print('Time elapsed: %.2f min' % ((time.time() - start_time)/60))
    print('Total Training Time: %.2f min' % ((time.time() - start_time)/60))
```

### What each training step is doing

1. Move data to the correct device and flatten it.
2. Run the model forward to get `logits`.
3. Compare logits with the true labels using cross-entropy.
4. Clear old gradients with `optimizer.zero_grad()`.
5. Backpropagate with `loss.backward()`.
6. Update parameters with `optimizer.step()`.

## 11. Replace MLP layers with LoRA layers

### Fill-in code

```python
model_lora = copy.deepcopy(model)

model_lora.layers[0] = LinearWithLoRAMerged(model_lora.layers[0], rank=4, alpha=8)
model_lora.layers[2] = LinearWithLoRAMerged(model_lora.layers[2], rank=4, alpha=8)
model_lora.layers[4] = LinearWithLoRAMerged(model_lora.layers[4], rank=4, alpha=8)
model_lora.to(DEVICE)
optimizer_lora = torch.optim.Adam(model_lora.parameters(), lr=learning_rate)
print(model_lora)

print(f'Test accuracy orig model:{compute_accuracy(model, test_loader, DEVICE):.2f}%')
print(f'Test accuracy LoRA model:{compute_accuracy(model_lora, test_loader, DEVICE):.2f}%')
```

### Why a deep copy is used

You first train the normal MLP.

Then you create a separate copy and replace its linear layers with LoRA versions. That lets you compare:

- original pretrained model
- LoRA-wrapped model

without destroying the original.

### Why the accuracy should initially stay similar

Again, the LoRA branch starts near zero, so the wrapped model should behave almost like the original model before LoRA fine-tuning.

## 12. Freeze the original linear layers

### Why this matters

This is the central LoRA idea.

We do **not** want to keep training the original base weights.

We only want to train the small adapter matrices `A` and `B`.

### Provided code

```python
def freeze_linear_layers(model):
    for child in model.children():
        if isinstance(child, nn.Linear):
            for param in child.parameters():
                param.requires_grad = False
        else:
            freeze_linear_layers(child)
```

### Why the recursion works

`model_lora` contains `LinearWithLoRAMerged` modules.

Each wrapper contains:

- `self.linear` which is an `nn.Linear`
- `self.lora` which is a `LoRALayer`

The recursive function walks into child modules and freezes only the inner `nn.Linear` parts, leaving `self.lora.A` and `self.lora.B` trainable.

## 13. Final LoRA fine-tuning step

The notebook uses:

```python
optimizer_lora = torch.optim.Adam(model_lora.parameters(), lr=learning_rate)
```

This works, but a slightly cleaner version is:

```python
optimizer_lora = torch.optim.Adam(
    filter(lambda p: p.requires_grad, model_lora.parameters()),
    lr=learning_rate
)
```

That way the optimizer only sees the parameters that are still trainable.

## 14. Quick mental model

When you feel lost, think of LoRA like this:

- a normal linear layer has one big matrix to train
- LoRA freezes that big matrix
- LoRA learns a small correction using two small matrices
- the model output becomes "original answer + small learned adjustment"

## 15. Most important concepts to remember

### `rank`

Controls how small the low-rank update is.

- smaller rank = fewer trainable parameters
- larger rank = more expressive update

### `alpha`

Controls how strongly the LoRA update affects the output.

In many LoRA implementations you will see scaling like `alpha / rank`.

This notebook uses a simpler version and scales directly by `alpha`.

### Why LoRA is useful

- fewer trainable parameters
- cheaper fine-tuning
- lower memory usage
- easy to attach to a pretrained model

## 16. A simple way to count LoRA parameters

For one full linear layer:

```python
in_dim * out_dim
```

For LoRA:

```python
in_dim * rank + rank * out_dim
```

Example:

- full layer: `784 * 256 = 200704`
- LoRA with `rank=4`: `784 * 4 + 4 * 256 = 4160`

That is a huge reduction in trainable parameters.

## 17. One practical warning

I did not run the full notebook in this workspace because `torch` is not currently installed here, so this walkthrough is based on the code structure and expected PyTorch behavior.

If you want, I can also turn this into:

- a fully solved notebook
- a simpler "LoRA for beginners" explanation with diagrams
- a version of the notebook with extra comments added to every code cell
