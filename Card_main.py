#! /usr/bin/python3
import Card_tools


while True:
    Card_tools.show_menu()
    action_str = input("请选择希望的操作:")
    print("您选择的操作是[%s]" % action_str)
    if action_str in ["1", "2", "3"]:
        if action_str == "1":
            Card_tools.new_card()
        elif action_str == "2":
            Card_tools.show_all()
        elif action_str == "3":
            Card_tools.search_card()
        pass

    elif action_str == "0":

        print("欢迎再次使用[名片管理系统]！")

        break

    else:
        print("您输入的不正确，请重新输入")