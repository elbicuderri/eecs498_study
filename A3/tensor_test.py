import torch

a = torch.tensor([-1, 1, 3, 4, 0, 5])

print(a)

out = torch.clamp(a, min=0)

print(out)

ac = a.detach().clone()

ac[ac > 0] = 1
ac[ac <= 0] = 0

print(ac)
print(a)