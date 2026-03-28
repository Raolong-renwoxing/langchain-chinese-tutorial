# Python Click 教程：构建可扩展、可组合的 CLI 应用

> **原文地址**：[Real Python - Python Click: Build Extensible and Composable CLI Apps](https://realpython.com/python-click/)
>
> **作者**：Leodanis Pozo Ramos
>
> **阅读时长**：约 1 小时 3 分钟
>
> **难度**：中级
>
> **标签**：DevOps、Python、工具

---

## 目录

- [简介](#简介)
- [为何选择 Click 进行 CLI 开发](#为何选择-click-进行-cli-开发)
- [安装与配置 Click：你的第一个 CLI 应用](#安装与配置-click你的第一个-cli-应用)
- [在 Click 应用中添加 Arguments](#在-click-应用中添加-arguments)
  - [添加基本 Arguments](#添加基本-arguments)
  - [使用路径 Arguments](#使用路径-arguments)
  - [接受可变参数 Arguments](#接受可变参数-arguments)
  - [接受文件 Arguments](#接受文件-arguments)
- [在 Click 应用中添加 Options](#在-click-应用中添加-options)
  - [添加单值 Options](#添加单值-options)
  - [创建多值 Options](#创建多值-options)
  - [多次指定同一个 Option](#多次指定同一个-option)
  - [将 Options 定义为布尔标志](#将-options-定义为布尔标志)
  - [创建功能开关](#创建功能开关)
  - [从多个选项中获取值](#从多个选项中获取值)
  - [从环境变量中获取 Options](#从环境变量中获取-options)
  - [提示用户输入值](#提示用户输入值)
- [为 Arguments 和 Options 提供参数类型](#为-arguments-和-options-提供参数类型)
- [在 Click 中创建子命令](#在-click-中创建子命令)
  - [立即注册子命令](#立即注册子命令)
  - [延迟注册子命令](#延迟注册子命令)
- [调整 Click 应用中的 Usage 和帮助信息](#调整-click-应用中的-usage-和帮助信息)
  - [为命令和 Options 编写文档](#为命令和-options-编写文档)
  - [为 Arguments 编写文档](#为-arguments-编写文档)
- [准备 Click 应用以进行安装和使用](#准备-click-应用以进行安装和使用)
  - [为 CLI 应用创建项目目录结构](#为-cli-应用创建项目目录结构)
  - [为 Click 项目编写 pyproject.toml](#为-click-项目编写-pyprojecttoml)
  - [创建虚拟环境并安装 Click 应用](#创建虚拟环境并安装-click-应用)
- [总结](#总结)

---

## 简介

借助 Click 库，你可以为 Python 自动化脚本和工具快速提供一个可扩展、可组合、用户友好的**命令行接口（CLI）**。无论你是开发者、数据科学家、DevOps 工程师，还是经常使用 Python 来自动化重复性任务的人，你都会非常欣赏 Click 及其独特功能。

在 Python 生态系统中，你会找到多个用于创建 CLI 的库，包括标准库中的 `argparse`、Typer 等。然而，Click 提供了一个健壮、成熟、直观且功能丰富的解决方案。

通过本教程，你将学习如何：

- 使用 Click 和 Python 创建命令行接口
- 为 CLI 应用添加 **arguments**、**options** 和 **子命令**
- 使用 Click 增强 CLI 应用的 **usage** 和**帮助页面**
- 准备 Click CLI 应用以进行**安装、使用和分发**

为了充分利用本教程，你应该对 Python 编程有良好的理解，包括装饰器（decorator）的使用。熟悉当前操作系统的命令行或终端也将有所帮助。

---

## 使用 Click 和 Python 创建命令行接口

Click 库让你能够为脚本和工具快速创建健壮、功能丰富且可扩展的命令行接口。该库可以显著加速你的开发过程，因为它允许你专注于应用程序的业务逻辑，而将 CLI 的创建和管理工作交给库本身来处理。

Click 是 Python 标准库中默认的 CLI 框架——argparse 模块的绝佳替代方案。接下来，你将了解是什么让 Click 与众不同。

---

## 为何选择 Click 进行 CLI 开发

与 argparse 相比，Click 提供了一个更灵活、更直观的框架来创建高度可扩展的 CLI 应用。它允许你以最少的代码渐进式地组合你的应用程序，而且即使你的 CLI 变得更大更复杂，代码仍然保持良好的可读性。

Click 的应用程序接口（API）非常直观和一致。该 API 利用 Python 装饰器，允许你快速为 CLI 添加 arguments、options 和子命令。

**函数**是 Click 驱动的 CLI 应用的基础。你需要编写函数，然后使用适当的装饰器包装它们来创建 arguments、commands 等。

Click 提供了几个值得称道的特性：

- **可延迟组合**：无需限制即可轻松组合
- **遵循 Unix 命令行约定**
- **支持从环境变量加载值**
- **支持自定义输入提示**
- **开箱即用的路径和文件处理**
- **支持任意嵌套命令（即子命令）**

你会发现 Click 还有许多其他酷炫特性。例如，Click 保留了所有 arguments、options 和 commands 的信息，因此它可以为 CLI 生成 Usage 和帮助页面，从而改善用户体验。

在处理用户输入方面，Click 对数据类型有很强的理解。正因如此，当用户提供错误类型的输入时，库会生成一致的错误信息。

现在你已经对 Click 最相关的特性有了基本了解，是时候动手编写你的第一个 Click 应用了。

---

## 安装与配置 Click：你的第一个 CLI 应用

与 argparse 不同，Click 不是 Python 标准库的一部分。这意味着你需要将 Click 作为 CLI 项目的依赖项进行安装才能使用该库。你可以使用 pip 从 PyPI 安装 Click。首先，你应该创建一个 Python 虚拟环境来工作。

**Windows**

```powershell
python -m venv venv
.\venv\Scripts\activate
pip install click
```

**Linux + macOS**

```bash
python -m venv venv
source venv/bin/activate
pip install click
```

使用前两个命令，你可以在工作目录中创建并激活一个名为 `venv` 的 Python 虚拟环境。环境激活后，使用 pip 安装 Click。

太棒了！你已经在一个全新的虚拟环境中安装了 Click。现在打开你最喜欢的代码编辑器，创建一个新的 `hello.py` 文件，并添加以下内容：

```python
import click

@click.command()
@click.version_option(version="1.0.0")
def hello():
    click.echo("Hello, World!")

if __name__ == "__main__":
    hello()
```

在这个文件中，首先导入 `click` 包，然后创建了一个名为 `hello()` 的函数。在这个函数中，使用 Click 的 `echo()` 函数而不是你熟悉的 `print()` 来向屏幕打印消息。

为什么要这样做呢？`echo()` 函数会在终端程序存在配置问题时进行一些错误纠正。它还支持输出中的颜色和其他样式。如果输出流是文件而非标准输出，它会自动移除任何样式。因此，在使用 Click 时，应该使用 `echo()` 来处理应用程序的输出。

你在这个函数上方使用了两个装饰器。`@click.command` 装饰器将 `hello()` 声明为一个名为 "hello" 的 Click 命令。`@click.version_option` 装饰器设置 CLI 应用的版本和名称。当你使用 `--version` 命令行选项运行应用时，这些信息会显示出来。

最后，添加 `if __name__ == "__main__"` 惯用法，以便将文件作为可执行程序运行时调用 `hello()` 函数。

从命令行运行这个应用试试：

```bash
python hello.py
```

运行脚本时不带参数，屏幕上会显示 `Hello, World!`。如果使用 `--version` 选项，你会得到应用程序的名称和版本信息。请注意，Click 会自动提供 `--help` 选项，你可以使用它来访问应用程序的主帮助页面。

太酷了！仅仅几行代码和 Click 的强大功能，你就创建了第一个 CLI 应用。这是一个最小的应用，但足以让你了解使用 Click 能够创建什么样的应用。继续你的 CLI 之旅吧，接下来你将学习如何让应用程序接受用户的输入参数。

---

## 在 Click 应用中添加 Arguments

在 CLI 开发中，**argument** 是命令用来执行其预期操作的必需或可选信息片段。命令通常接受 arguments，你可以作为命令行上的空格分隔或逗号分隔列表来提供这些 arguments。

在本节中，你将学习如何在 Click 应用程序中获取命令行 arguments。你将从最基本形式的 arguments 开始，然后逐步介绍不同类型的 arguments，包括路径、文件、环境变量等。

### 添加基本 Arguments

你可以使用 `@click.argument` 装饰器来让你的 Click 应用接受并解析你直接在命令行提供的 arguments。Click 将最基础的 arguments 解析为字符串，然后你可以将它们传递给底层函数。

为了说明，假设你想创建一个小型的 CLI 应用来模拟 Unix 的 `ls` 命令。在最简化的形式下，这个命令接受一个目录作为 argument 并列出其内容。

如何用 Click 和 Python 来模拟这个命令行为？

```python
import click
from pathlib import Path

@click.command()
@click.argument("path")
def cli(path):
    path = Path(path)
    if not path.exists():
        click.echo(f"Path '{path}' does not exist.")
        exit(1)
    if not path.is_dir():
        click.echo(f"'{path}' is not a directory.")
        exit(1)
    for entry in path.iterdir():
        click.echo(entry.name)
    click.echo()
```

这是你的 `ls` 命令模拟器应用的第一个版本。首先从 `pathlib` 导入 `Path` 类，你将使用这个类来高效地管理应用程序中的路径。然后像往常一样导入 `click`。

你的 `ls` 模拟器需要一个单独的函数来执行其预期任务。你把这个函数命名为 `cli()`，这是一种常见做法。Click 应用通常将入口命令命名为 `cli()`。

在这个示例中，使用 `@click.command` 装饰器定义一个命令。然后使用 `@click.argument` 装饰器和字符串 `"path"` 作为 argument 来添加一个新的命令行 argument。

请注意，命令行 argument 的名称必须与 `cli()` 的参数名称相同。这样，你就可以将用户输入直接传递到处理代码中。

在 `cli()` 内部，使用用户输入创建一个新的 `Path` 实例。然后检查输入路径。如果路径不存在，则通知用户并以适当的退出状态退出应用程序。如果路径存在，则 `for` 循环列出目录内容，模拟 Unix `ls` 命令的行为。

`cli()` 末尾对 `click.echo()` 的调用允许你在输出末尾添加一个新行，以匹配 `ls` 的行为。

还不到二十行 Python 代码，效果如何？很棒！然而，Click 为你提供了一个更好的方法。你可以利用 Click 的强大功能来自动处理应用程序中的文件路径。

### 使用路径 Arguments

`@click.argument` 装饰器接受一个名为 `type` 的参数，你可以用它来定义 argument 的目标数据类型。此外，Click 提供了一套丰富的自定义类，让你能够一致地处理不同的数据类型，包括路径。

在下面的示例中，你使用 Click 的功能重写了 `ls` 应用：

```python
import click
from pathlib import Path

@click.command()
@click.argument(
    "path",
    type=click.Path(exists=True, file_okay=False, readable=True, path_type=Path)
)
def cli(path):
    path = Path(path)
    for entry in path.iterdir():
        click.echo(entry.name)
    click.echo()
```

在这个新版本的 `ls.py` 中，你向 `@click.argument` 的 `type` 参数传递了一个 `click.Path` 对象。有了这个补充，Click 会将任何输入视为路径对象。

为了实例化这个示例中的 `click.Path()` 类，你使用了几个参数：

- **exists**：如果设为 `True`，则 Click 将确保路径存在
- **file_okay**：如果设为 `False`，则 Click 将确保输入路径不指向文件
- **readable**：如果设为 `True`，则 Click 将确保可以读取目标目录的内容
- **path_type**：如果设为 `pathlib.Path`，则 Click 会将输入转换为 `Path` 对象

有了这些设置，你的 `cli()` 函数更加简洁。它只需要 `for` 循环来列出目录内容。

同样，如果你使用有效的目录路径运行应用，会列出目录内容。如果目标目录不存在，Click 会为你处理这个问题。你会得到一条漂亮的 Usage 消息和一条描述当前问题的错误消息。

### 接受可变参数 Arguments

在 Click 的术语中，**可变参数（variadic argument）** 是指在命令行接受不定数量输入值的 argument。这种类型的 argument 在 CLI 开发中非常常见。例如，Unix 的 `ls` 命令就利用了这个特性，允许你同时处理多个目录。

`@click.argument` 装饰器接受一个名为 `nargs` 的参数，允许你预定义一个 argument 在命令行可以接受的值数量。如果将 `nargs` 设为 `-1`，则底层 argument 将把不定数量的输入值收集到一个元组中。

以下是你如何利用 `nargs` 来接受 `ls` 模拟器中的多个目录：

```python
import click
from pathlib import Path

@click.command()
@click.argument(
    "paths",
    nargs=-1,
    type=click.Path(exists=True, file_okay=False, readable=True, path_type=Path)
)
def cli(paths):
    for path in paths:
        path = Path(path)
        click.echo(f"{path}/:")
        for entry in path.iterdir():
            click.echo(entry.name)
        click.echo()
```

在第一个突出显示的行中，你将 argument 的名称从 `"path"` 改为 `"paths"`，因为现在这个 argument 将接受多个目录路径。然后将 `nargs` 设为 `-1` 以表示这个 argument 将在命令行接受多个值。

在 `cli()` 函数中，更改变量名称以匹配命令行 argument 的名称。然后开始循环遍历输入路径。条件语句打印当前目录的名称，模拟原始 `ls` 命令的行为。

然后运行通常的循环来列出目录内容，最后调用 `echo()` 以在每个目录的内容后面添加一个新的空白行。

现在，当你向命令行传递多个目标目录时，你的自定义 `ls` 命令的行为与原始的 Unix `ls` 命令类似。太棒了！你已经学会了如何在 Click 中实现可变参数 arguments。

### 接受文件 Arguments

Click 提供了一个名为 `File` 的参数类型，你可以用它来在命令行 argument 必须是文件时使用。有了 `File`，你可以声明某个参数是一个文件。你还可以声明应用程序是否应该打开文件进行读取或写入。

为了说明如何使用 `File` 参数类型，假设你想模拟 Unix `cat` 命令的基本功能。这个命令依次读取文件并将其内容写入标准输出（即你的屏幕）：

```python
import click

@click.command()
@click.argument("files", type=click.File(), nargs=-1)
def cli(files):
    for file in files:
        click.echo(file.read())
    click.echo()
```

在这个示例中，将 `type` 参数设为 `click.File()`。默认情况下，Click 以读取模式（`"r"`）打开文件。

在 `cli()` 中，开始一个 `for` 循环来遍历输入文件并将它们的内容打印到屏幕。请注意，一旦命令运行完毕，你不需要担心关闭每个文件。`File` 类型会自动为你关闭它。

你的 `cat.py` 脚本的工作方式与 Unix `cat` 命令非常相似。它接受命令行上的多个文件，打开它们进行读取，读取它们的内容，然后依次将它们打印到屏幕。干得漂亮！

---

## 在 Click 应用中添加 Options

**命令选项（Command options）** 是 Click 应用程序的另一个强大功能。选项是有名称的非必需 arguments，用于修改命令的行为。你使用特定名称将选项传递给命令，在 Unix 系统上这个名称通常带有一个短横线（`-`）或两个短横线（`--`）作为前缀。在 Windows 上，你可能还会发现其他前缀的选项，例如斜杠（`/`）。

因为选项有名称，它们增强了 CLI 应用程序的可用性。在 Click 中，选项可以做与 arguments 相同的操作。此外，选项还有一些额外功能。例如，选项可以：

- 提示输入值
- 作为标志或功能开关
- 从环境变量中拉取值

与 arguments 不同，选项只能接受固定数量的输入值，这个数量默认为 1。此外，你可以使用多个选项多次指定一个选项，但不能对 arguments 这样做。

### 添加单值 Options

要向 Click 命令添加选项，你将使用 `@click.option` 装饰器。这个装饰器的第一个参数将保存选项的名称。

CLI 选项通常有长名称和短名称。长名称通常描述选项的作用，而短名称通常是单个字母的快捷方式。对于 Click，带单个前导短横线的名称是短名称，带两个前导短横线的名称是长名称。

在 Click 中，最基本类型的选项是单值选项，它在命令行接受一个 argument。如果你不为选项值提供参数类型，Click 会假定为 `click.STRING` 类型。

为了说明如何使用 Click 创建选项，假设你想编写一个模拟 Unix `tail` 命令的 CLI 应用程序。这个命令显示文本文件的末尾部分：

```python
import click
from collections import deque

@click.command()
@click.option("-n", "--lines", default=10, type=click.INT)
@click.argument("file", type=click.File())
def cli(file, lines):
    lines = deque(file, maxlen=lines)
    for line in lines:
        click.echo(line, nl=False)
    click.echo()
```

在这个示例中，首先从 `collections` 模块导入 `deque` 数据类型。你将使用这种类型来快速从输入文件获取最后几行。然后像往常一样导入 `click`。

调用 `@click.option` 装饰器向 Click 命令添加一个新选项。这次调用中的前两个参数分别提供选项的短名称和长名称（`-n` 和 `--lines`）。

因为用户输入必须是整数，你使用 `click.INT` 来定义参数的类型。`tail` 的默认行为是显示最后十行，所以你将 `default` 设为 `10`，并发现了 Click 选项的另一个酷炫特性——它们可以有默认值。

接下来，添加一个名为 `"file"` 的 argument，其类型为 `click.File()`。

在 `cli()` 中，接受 `file` 和 `lines` 作为 arguments。然后使用 `deque` 对象循环遍历最后几行。这个特定的 `deque` 对象只能存储最多 `lines` 个项目。这保证了你从输入文件末尾获得所需数量的行。

你的自定义 `tail` 命令的工作方式与原始的 Unix `tail` 命令类似。它接受一个文件，默认显示最后十行。如果你使用 `--lines` 选项提供不同的行数，该命令只从输入文件末尾显示你想要的行数。

当你查看 `tail` 命令的帮助页面时，你会看到 `-n` 或 `--lines` 选项现在显示在 Options 标题下。默认情况下，你还会获得有关选项参数类型（在本例中是一个整数）的信息。

### 创建多值 Options

有时你需要实现一个在命令行接受多个输入值的选项。与 arguments 不同，Click 选项只支持固定数量的输入值。你可以使用 `@click.option` 的 `nargs` 参数来配置这个数字。

下面的示例接受一个需要两个输入值（宽度和高度）的 `--size` 选项：

```python
import click

@click.command()
@click.option("--size", nargs=2, type=click.INT, default=(100, 50))
def cli(size):
    width, height = size
    click.echo(f"Width: {width}, Height: {height}")
```

在这个示例中，你在定义 `--size` 选项的 `@click.option` 装饰器调用中将 `nargs` 设为 `2`。这个设置告诉 Click 该选项将在命令行接受两个值。

`--size` 选项在命令行接受两个输入值。Click 将这些值存储在一个元组中，你可以在 `cli()` 函数中处理它。注意 `--size` 选项不接受少于或多于两个的输入值。

Click 提供了另一种创建多值选项的方法。你可以使用元组而不是 `@click.option` 的 `nargs` 参数来设置 `type` 参数：

```python
import click

@click.command()
@click.option("--size", type=(click.INT, click.INT), default=(100, 50))
def cli(size):
    width, height = size
    click.echo(f"Width: {width}, Height: {height}")
```

在这个替代实现中，将 `type` 参数设为一个整数元组。请注意，你也可以使用 `click.Tuple` 参数类型来获得相同的结果。使用这种类型会更加明确，你只需要做 `type=click.Tuple([int, int])`。

通过使用元组作为 `type` 参数，你可以自定义元组中每个项目的参数类型，这在某些情况下可能非常方便。

为了说明 `click.Tuple` 如何帮助你，请考虑以下示例：

```python
import click

@click.command()
@click.option("--profile", type=click.Tuple([str, str]))
def cli(profile):
    name, language = profile
    click.echo(f"Name: {name}, Language: {language}")
```

在这个示例中，`--profile` 选项接受一个两项元组。第一项应该是代表一个人名字的字符串。

### 多次指定同一个 Option

有时，你可能希望允许用户多次指定同一个选项。Click 的选项默认只能接受一个值，但你可以通过设置 `multiple=True` 来改变这种行为。

例如，你想创建一个允许用户多次指定要处理的文件名的选项：

```python
import click

@click.command()
@click.option("--name", multiple=True)
def cli(names):
    for name in names:
        click.echo(name)
```

在这个示例中，`--name` 选项可以接受多个值。用户可以这样使用：

```bash
python cli.py --name Alice --name Bob --name Charlie
```

### 将 Options 定义为布尔标志

**布尔标志（Boolean flags）** 是 Click 中另一种有趣的选项类型。顾名思义，布尔标志用于表示布尔值（True 或 False）。在 CLI 应用程序中，布尔标志通常作为开关使用，当用户传递标志时启用某个功能，当用户省略标志时禁用该功能。

要在 Click 中创建布尔标志，你需要使用 `@click.option` 装饰器的 `is_flag` 参数：

```python
import click

@click.command()
@click.option("--verbose", is_flag=True)
def cli(verbose):
    if verbose:
        click.echo("Verbose mode is enabled.")
    else:
        click.echo("Verbose mode is disabled.")
```

在这个示例中，`--verbose` 选项是一个布尔标志。当用户传递 `--verbose` 时，`verbose` 参数将为 `True`；当用户省略 `--verbose` 时，`verbose` 参数将为 `False`。

布尔标志在 CLI 应用程序中非常常见，因为它们提供了一种简单直观的方式来控制应用程序的行为。

### 创建功能开关

布尔标志通常用于创建**功能开关**，允许用户启用或禁用应用程序的特定功能：

```python
import click

@click.command()
@click.option("--quiet", is_flag=True, help="Suppress output messages.")
@click.option("--debug", is_flag=True, help="Enable debug mode.")
def cli(quiet, debug):
    if debug:
        click.echo("Debug mode is enabled.")
    if not quiet:
        click.echo("Application is running...")
```

### 从多个选项中获取值

有时你可能希望从多个可能的选项中获取值。Click 提供了 `choice` 参数，允许你定义选项的有效值列表：

```python
import click

@click.command()
@click.option("--color", type=click.Choice(["red", "green", "blue"]))
def cli(color):
    click.echo(f"Selected color: {color}")
```

### 从环境变量中获取 Options

Click 支持从环境变量中获取选项值。这对于配置敏感信息或常用设置非常有用：

```python
import click
import os

@click.command()
@click.option("--username", envvar="APP_USERNAME")
def cli(username):
    click.echo(f"Username: {username}")
```

在这个示例中，如果用户没有在命令行提供 `--username` 选项，Click 会从 `APP_USERNAME` 环境变量中获取值。

### 提示用户输入值

Click 允许你在用户未提供选项时提示他们输入值。这通过 `prompt` 参数实现：

```python
import click

@click.command()
@click.option("--name", prompt=True)
def cli(name):
    click.echo(f"Hello, {name}!")
```

如果用户运行 `python cli.py` 而不提供 `--name` 选项，Click 会自动提示用户输入。

---

## 为 Arguments 和 Options 提供参数类型

Click 提供了丰富的内置参数类型，让你可以轻松处理各种数据。以下是一些常用的参数类型：

- **click.STRING**：字符串（默认）
- **click.INT**：整数
- **click.FLOAT**：浮点数
- **click.BOOL**：布尔值
- **click.Choice**：选项列表
- **click.File**：文件
- **click.Path**：路径
- **click.DateTime**：日期时间

你还可以创建自定义参数类型来满足特定需求：

```python
import click

class EmailType(click.ParamType):
    name = "email"

    def convert(self, value, param, ctx):
        if "@" not in value:
            self.fail(f"{value!r} is not a valid email address", param, ctx)
        return value

@click.command()
@click.option("--email", type=EmailType())
def cli(email):
    click.echo(f"Email: {email}")
```

---

## 在 Click 中创建子命令

随着 CLI 应用程序变得越来越复杂，你可能希望将相关功能组织成**子命令（subcommands）**。在 Click 中，你可以使用 `@click.group` 装饰器创建一个命令组，然后使用 `@click.command` 装饰器向该组添加子命令。

### 立即注册子命令

以下是一个演示子命令用法的示例：

```python
import click

@click.group()
def cli():
    pass

@cli.command()
def init():
    click.echo("Initialized the project.")

@cli.command()
def build():
    click.echo("Built the project.")

@cli.command()
def run():
    click.echo("Ran the project.")

if __name__ == "__main__":
    cli()
```

在这个示例中，`cli()` 是主命令组，而 `init`、`build` 和 `run` 是子命令。

你可以使用 `cli.py init`、`cli.py build` 和 `cli.py run` 来调用子命令。

### 延迟注册子命令

对于更复杂的应用程序，你可能希望将子命令分散到多个模块中。Click 允许你使用 `add_command()` 方法延迟注册子命令：

假设你有以下项目结构：

```
calc/
├── calc.py
└── commands.py
```

`commands.py` 文件包含所有子命令的实现：

```python
import click

@click.command()
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def add(a, b):
    click.echo(a + b)

@click.command()
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def sub(a, b):
    click.echo(a - b)

@click.command()
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def mul(a, b):
    click.echo(a * b)

@click.command()
@click.argument("a", type=click.FLOAT)
@click.argument("b", type=click.FLOAT)
def div(a, b):
    click.echo(a / b)
```

然后在 `calc.py` 中导入并注册这些子命令：

```python
import click
import commands

@click.group()
def cli():
    pass

cli.add_command(commands.add)
cli.add_command(commands.sub)
cli.add_command(commands.mul)
cli.add_command(commands.div)

if __name__ == "__main__":
    cli()
```

在 `calc.py` 文件中，首先更新导入以包含 `commands` 模块，该模块提供了应用程序子命令的实现。然后使用 `add_command()` 方法在 `cli` 组中注册这些子命令。

一般来说，当你的 CLI 应用程序由多个模块组成且命令分散在这些模块中时，你会使用 `add_command()` 来注册子命令。

---

## 调整 Click 应用中的 Usage 和帮助信息

Click 提供了几个内置功能来增强 CLI 应用程序的帮助页面。

### 为命令和 Options 编写文档

你可以使用 `help` 参数为命令和选项提供文档：

```python
import click

@click.command()
@click.option("--name", default="World", help="The name to greet.")
@click.option("--verbose", is_flag=True, help="Enable verbose output.")
def hello(name, verbose):
    if verbose:
        click.echo(f"About to greet {name}...")
    click.echo(f"Hello, {name}!")
```

运行 `python hello.py --help` 会显示：

```
Usage: hello.py [OPTIONS]

Options:
  --name TEXT      The name to greet. [default: World]
  --verbose        Enable verbose output.
  --help           Show this message and exit.
```

### 为 Arguments 编写文档

你也可以为 arguments 提供文档，使用 `@click.argument` 装饰器的 `help` 参数：

```python
import click

@click.command()
@click.argument("filename", help="The file to process.")
def cli(filename):
    click.echo(f"Processing {filename}...")
```

---

## 准备 Click 应用以进行安装和使用

一旦你创建了一个 Click CLI 应用程序，你可能希望将其作为可安装的包进行分发，以便用户可以轻松安装和使用它。

### 为 CLI 应用创建项目目录结构

对于一个名为 `calc` 的计算器 CLI 应用，你的项目结构可能如下所示：

```
calc/
├── __init__.py
├── __main__.py
└── commands.py

pyproject.toml

README.md
```

`calc/` 文件夹是项目的根目录。

### 为 Click 项目编写 pyproject.toml

`pyproject.toml` 是一个 TOML 文件，指定了项目的构建系统和许多其他配置。在现代 Python 中，这个文件在某种程度上取代了 `setup.py` 脚本。

```toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "calc"
version = "1.0.0"
description = "A simple calculator CLI application"
readme = "README.md"
requires-python = ">=3.7"
dependencies = [
    "click",
]

[project.scripts]
calc = "calc.__main__:cli"
```

`README.md` 提供了项目描述和安装运行说明。为你的项目添加描述性且详细的 `README.md` 文件是编程的最佳实践，特别是如果你计划将项目作为开源解决方案发布到 PyPI。

`__init__.py` 使 `calc/` 成为一个 Python 包。`__main__.py` 提供应用程序的入口点脚本。`commands.py` 提供应用程序的子命令。

### 创建虚拟环境并安装 Click 应用

创建虚拟环境并安装依赖：

```bash
python -m venv venv
source venv/bin/activate  # Windows: .\venv\Scripts\activate
pip install -e .
```

安装后，你可以运行 `calc` 命令：

```bash
calc add 3 8
calc sub 10 5
calc mul 4 7
calc div 20 4
```

---

## 总结

本教程为你提供了使用 Python Click 库创建命令行接口的全面指南。你学习了：

- Click 库的基础知识以及为何它是创建 CLI 应用程序的绝佳选择
- 安装 Click 并创建你的第一个 CLI 应用程序
- 在 Click 应用中添加 arguments（基本参数、路径参数、可变参数、文件参数）
- 在 Click 应用中添加 options（单值选项、多值选项、布尔标志、功能开关等）
- 为 Arguments 和 Options 提供参数类型
- 使用子命令组织应用
- 调整 CLI 应用的帮助页面
- 将 CLI 应用作为包进行安装与分发

Click 是一个功能强大且灵活的库，可以帮助你快速创建专业级的命令行接口。借助其直观的 API 和丰富的功能，Click 使得构建 CLI 应用变得轻松愉快。

无论你是初学者还是有经验的开发者，Click 都是你工具箱中不可或缺的利器。

---

> **备注**：本翻译尽可能完整地呈现了原文内容。如需获取最新完整版本，请参阅原文地址：https://realpython.com/python-click/
