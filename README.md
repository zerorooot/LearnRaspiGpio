买了个树莓派，原本就像拿来配合aria2下种子用的，不过这个gpio不能浪费了，就上网找了找教程，学了一下.
解释：
1.gpio.py --> 控制led灯亮灭
2.gpio-pwm.py --> 在控制led灯亮灭基础上加入了pwm模式，可以控制灯泡的亮度
3.g.py --> 控制rbg灯亮灭
4.g-pwm.py --> 在控制rbg灯亮灭基础上加入了pwm模式，可以控制rbg灯的亮度
5.randoms.py --> xjb闪rbg灯
6.gt.py --> 通过触摸触碰模块来改变rgb灯的颜色
6.fm.py --> 控制蜂鸣器
7.fmt.py --> 通过触摸触碰模块来控制蜂鸣器
digit.py --> 数码管显示当前系统秒数
input.py --> gpio输入模式
touch.py --> 触碰模块demo
demo.py --> 最基本的代码
heart.py --> 心跳传感器控制/改变rgb灯的颜色
tm1637  --> tm1637数码管demo
