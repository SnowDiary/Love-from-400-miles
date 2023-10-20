# 游戏的脚本可置于此文件中。

# 声明此游戏使用的角色。颜色参数可使角色姓名着色。

define e = Character("Ju33Huang22")


# 游戏在此开始。

label start:

    # 显示一个背景。此处默认显示占位图，但您也可以在图片目录添加一个文件
    # （命名为 bg room.png 或 bg room.jpg）来显示。

    image bg1 = "images/bg/bg1.png"

    scene bg1

    # 显示角色立绘。此处使用了占位图，但您也可以在图片目录添加命名为
    # eileen happy.png 的文件来将其替换掉。

    image eileen happy = "images/character/test1.png"

    show eileen happy

    # 此处显示各行对话。

    e "{cps=20}氦，我是Ju33Huang22{/cps}"

    e "{cps=20}感谢你游玩由SquareCircle旗下品牌SnowDiary的第一款测试向Galgame！{/cps}"

    e "{cps=20}Love from 400 miles 是基于 Ren'Py 进行开发的，目前仍在测试阶段{/cps}"

    menu:

        e "{cps=20}接下来请尝试切换支线{/cps}"

        "支线1":

            jump Line_1

        "支线2":

            jump Line_2


label Line_1:
    e "{cps=20}这里是支线1{/cps}"

    e "{cps=20}然后直接从支线1跳到结尾{/cps}"

    jump end

label Line_2:
    e "{cps=20}这里是支线2{/cps}"

    e "{cps=20}然后直接从支线2跳到结尾{/cps}"

    jump end

label end:
    e "{cps=20}最后，请开始协助我们测试这款游戏！{/cps}"


    # 此处为游戏结尾。

    return
