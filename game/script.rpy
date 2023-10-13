# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("Ju33Huang22")


# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    scene bg room

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    show eileen happy

    # 此处显示各行对话。

    e "氦，我是Ju33Huang22"

    e "感谢你游玩由SquareCircle旗下品牌SnowDiary的第一款测试向Galgame！"

    e "Love from 400 miles 是基于 Ren'Py 进行开发的，并且作为第一个SnowDiary测试向的GalGame将完全开源。（https://github.com/SnowDiary/Love from 400 miles）"

    e "最后，请开始协助我们测试这款游戏！"

    # 此处为游戏结尾。

    return
