---
layout: '@layouts/SlideLayout.astro'
title: Un test de slides
date: 2025
extra:
- math
---

## Subsection

<kbd>CTRL</kbd> + <kbd>ALT</kbd> + <kbd>Delete</kbd>

### Subsubsection

<mark>Highlight</mark> some text

#### h4

$$ \sqrt{3x-1}+(1+x)^2 $$

A **bold** and _emphasis_ text.

> Une citation
> sur deux lignes

---

:::correction
Une correction
:::

:::tip
Un petit tip
:::

:::link
[Un lien](/test) et une url : <https://www.google.fr>
:::

:::warn
Attention ici !
:::

:::strong
Une balise strong
:::

:::exo
Un exercice
:::

---
layout: section
---

# Une section

---

# Titre

```python
class A():
	def __init__(self, x):
		self.x = x
		print(x)
		return x

def f(y):
	return y

a = A()
f(2)
```
