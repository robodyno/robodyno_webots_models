# Robodyno - Webots 仿真模型

## 安装

### Webots

Webots 的安装请参考 [Webots 官方文档](https://cyberbotics.com/doc/guide/installation-procedure)。为了能够使用 Robodyno 的仿真模型，你需要安装 Webots R2023a 或者更新的版本。

### Robodyno

Robodyno 的软件包可以通过 pip 安装，建议使用 1.6.1 或者更新的版本。安装命令如下：

```bash
pip install robodyno >= 1.6.1
```

## 使用

### PROTO

Robodyno 提供了一系列的 [Webots PROTO](https://cyberbotics.com/doc/reference/proto)，存放在 `protos` 目录下，可以用于创建仿真模型。

其中，机械零件的 PROTO 文件存放在 `protos/objects` 目录下，其余的可控制设备的 PROTO 文件按类别存放在独立的目录下，例如 `protos/joints` 目录下存放了所有的关节设备。

### 示例

所有的示例存放在 `worlds` 目录下，可以通过 Webots 的 `File -> Open World` 菜单打开。示例中包含了一些典型的机械臂模型，每个模型都绑定了一个简单的控制器，可以通过指定关节的目标位置来控制机械臂的运动。控制器的源代码存放在 `controllers` 目录下。
