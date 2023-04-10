import os
'''comments:
        1.新增.txt/.mp4/.mov/.raw格式命名
        2.文件夹可包含其他文件夹在内
        3.不同格式文件在同一文件夹下也可命名
        4.新增错误异常处理，程序合理化运行
        5.新增指定序号开始命名(V1.4)
        6.修改一张图命名错误问题
    author:
        colin
    data:  2021/10/25'''
def get_filename(file_dir):

    '''筛选命名文件'''

    img_list = []

    list = os.listdir(file_dir)

    select_type = input("输入要命名的文件类型: 1.jpg 2.txt 3.mp4 4.mov 5.raw")

    for i in range(0,len(list)):
        if select_type == "1" or select_type == "jpg":
            if os.path.splitext(list[i])[1] == ".jpg":
                path = os.path.join(file_dir,list[i])
                img_list.append(path)
        elif select_type == "2" or select_type == "txt":
            if os.path.splitext(list[i])[1] == ".txt":
                path = os.path.join(file_dir,list[i])
                img_list.append(path)
        elif select_type == "3" or select_type == "mp4":
            if os.path.splitext(list[i])[1] == ".mp4":
                path = os.path.join(file_dir,list[i])
                img_list.append(path)
        elif select_type == "4" or select_type == "mov":
            if os.path.splitext(list[i])[1] == ".mov":
                path = os.path.join(file_dir,list[i])
                img_list.append(path)
        elif select_type == "5" or select_type == "raw":
            if os.path.splitext(list[i])[1] == ".raw":
                path = os.path.join(file_dir,list[i])
                img_list.append(path)
    return img_list
def rename():
    path_name = input("请输入所需命名图片文件夹绝对路径：")
    path = os.path.join(path_name)
    img_original = os.listdir(path)
    img_list = get_filename(path_name)
    # img_list.sort(key=lambda x: int((x.replace("Q","").split('.')[0]) or (x.replace("P","").split('.')[0])))#按照数字进行排序后按顺序读取文件夹下的图片
    last = os.path.splitext(img_list[1])[1]
    count = len(img_list)
    if count < 999:
        y = 3
    elif count >= 1000:
        y = 4
    else:
        y = 5
    list_i = 1
    w1 = True
    w2 = True
    while w1:
        i = int(input("请输入从几号开始命名："))
        select = input("请选择所需要的命名方法，A：序列+原图后缀，B：序列+所需后缀,C：同一系列命名")
        if select == "A" or select == "a" or select == "B" or select == "b" or select == "C" or select == "c" :
            while w2:
                try:
                    x = int(input('请输入一组图片包含的张数:'))
                    if select == 'A' or select == "a":
                        name = input("输入所需后缀：")
                        if x == 1:
                            num_i = i
                            for item in img_list:
                                if list_i % x == 0:
                                    os.rename(os.path.join(path_name, item),
                                              os.path.join(path_name, ((str(num_i)).zfill(
                                                  y) + "_" + name + "_" + item[len(path_name)+1:])))
                                list_i += 1
                                # num_i = int(list_i / x) + i
                                num_i += 1
                                pass
                        if x == 2:
                            num_i = i
                            for item in img_list:
                                if list_i % x == 1:
                                    os.rename(os.path.join(path_name, item),
                                              os.path.join(path_name, ((str(num_i)).zfill(y).zfill(y) +"_" + name + '_' + item[len(path_name)+1:])))
                                if list_i % x == 0:
                                    os.rename(os.path.join(path_name, item),
                                              os.path.join(path_name, ((str((num_i)-1)).zfill(y) + "_" + name + '_' + item[len(path_name)+1:])))
                                list_i += 1
                                num_i = int(list_i / x) + i
                                pass
                        if x == 3:
                            num_i = i
                            for item in img_list:
                                if list_i % x == 1:
                                    os.rename(os.path.join(path_name, item),
                                              os.path.join(path_name,((str(num_i)).zfill(y) + "_" + name + "_" + item[len(path_name)+1:])))
                                if list_i % x == 2:
                                    os.rename(os.path.join(path_name, item),
                                              os.path.join(path_name, ((str(num_i)).zfill(y) + "_" + name + "_" + item[len(path_name)+1:])))
                                if list_i % x == 0:
                                    os.rename(os.path.join(path_name, item),
                                              os.path.join(path_name, ((str((num_i)-1)).zfill(y) + "_" + name + "_" + item[len(path_name)+1:])))
                                list_i += 1
                                num_i = int(list_i/x) + i
                                pass
                        if x == 4:
                            num_i = i
                            for item in img_list:
                                if list_i % x == 1:
                                    os.rename(os.path.join(path_name, item),
                                              os.path.join(path_name, ((str(num_i)).zfill(y) + "_" + name + "_" + item[len(path_name)+1:])))
                                if list_i % x == 2:
                                    os.rename(os.path.join(path_name, item),
                                              os.path.join(path_name, ((str(num_i)).zfill(y) + "_" + name + "_" + item[len(path_name)+1:])))
                                if list_i % x == 3:
                                    os.rename(os.path.join(path_name, item),
                                              os.path.join(path_name, ((str(num_i)).zfill(y) + "_" + name + "_" + item[len(path_name)+1:])))
                                if list_i % x == 0:
                                    os.rename(os.path.join(path_name, item),
                                              os.path.join(path_name, ((str((num_i)-1)).zfill(y) + "_" + name + "_" + item[len(path_name)+1:])))
                                list_i += 1
                                num_i = int(list_i / x) + i
                        pass
                    if select == 'B' or select == "b":
                        xilie = str(input('请输入你想要的系列名称：'))
                        list_1 = list(xilie.split())
                        if x == 1:
                            num_i = i
                            for item in img_list:
                                if list_i % x == 0:
                                    os.rename(os.path.join(path_name, item),
                                              os.path.join(path_name, ((str(num_i)).zfill(y) + '_' + list_1[
                                                      0] + last)))  # 第二张命名
                                list_i += 1
                                num_i += 1
                                pass
                        if x == 2:
                            num_i = i
                            for item in img_list:
                                if list_i % x == 1:
                                    os.rename(os.path.join(path_name, item),
                                              os.path.join(path_name, ((str(num_i)).zfill(y) + '_' + list_1[0] + last)))  # 第一张命名
                                if list_i % x == 0:
                                    os.rename(os.path.join(path_name, item),
                                              os.path.join(path_name, ((str((num_i)-1)).zfill(y) + '_' + list_1[1] + last)))  # 第二张命名
                                list_i += 1
                                num_i = int(list_i / x) + i
                                pass
                        if x == 3:
                            num_i = i
                            for item in img_list:
                                if list_i % x == 1:
                                    os.rename(os.path.join(path_name, item),
                                              os.path.join(path_name, ((str(num_i)).zfill(y) + '_' + list_1[0] + last)))  # 第一张命名
                                if list_i % x == 2:
                                    os.rename(os.path.join(path_name, item), os.path.join(path_name, ((str(num_i)).zfill(y) + '_' + list_1[1] + last)))  # 第二张命名
                                if list_i % x == 0:
                                    os.rename(os.path.join(path_name, item), os.path.join(path_name, ((str((num_i)-1)).zfill(y) + '_' + list_1[2] + last)))  # 第三张命名
                                list_i += 1
                                num_i = int(list_i / x) + i
                                pass
                        if x == 4:
                            num_i = i
                            for item in img_list:
                                if list_i % x == 1:
                                    os.rename(os.path.join(path_name, item),
                                              os.path.join(path_name, ((str(num_i)).zfill(y) + '_' + list_1[0] + last)))  # 第一张命名
                                if list_i % x == 2:
                                    os.rename(os.path.join(path_name, item), os.path.join(path_name, ((str(num_i)).zfill(y) + '_' + list_1[1] + last)))  # 第二张命名
                                if list_i % x == 3:
                                    os.rename(os.path.join(path_name, item), os.path.join(path_name, ((str(num_i)).zfill(y) + '_' + list_1[2] + last)))  # 第三张命名
                                if list_i % x == 0:
                                    os.rename(os.path.join(path_name, item), os.path.join(path_name, ((str((num_i)-1)).zfill(y) + '_' + list_1[3] + last)))  # 第四张命名
                                list_i += 1
                                num_i = int(list_i / x) + i
                                pass
                    if select == 'C' or select == "c":
                        name = input("输入后缀序列所需")
                        name_num = [1, 2, 3, 4]
                        if x == 1:
                            num_i = i
                            for item in img_list:
                                if list_i % x == 0:
                                    os.rename(os.path.join(path_name, item), os.path.join(path_name, ((str(num_i)).zfill(y) + '_' + name + '_' + str(
                                        name_num[0]) + last)))  # 第二张命名
                                list_i += 1
                                num_i += 1
                                pass
                        if x == 2:
                            num_i = i
                            for item in img_list:
                                if list_i % x == 1:
                                    os.rename(os.path.join(path_name, item), os.path.join(path_name, ((str(num_i)).zfill(y) + '_' + name + '_' + str(name_num[0]) + last)))
                                if list_i % x == 0:
                                    os.rename(os.path.join(path_name, item), os.path.join(path_name, ((str((num_i)-1)).zfill(y) + '_' + name + '_' + str(
                                        name_num[1]) + last)))  # 第二张命名
                                list_i += 1
                                num_i = int(list_i / x) + i
                                pass
                        if x == 3:
                            num_i = i
                            for item in img_list:
                                if list_i % x == 1:
                                    os.rename(os.path.join(path_name, item), os.path.join(path_name, ((str(num_i)).zfill(y) + '_' + name + '_' + str(name_num[0]) + last)))  # 第一张命名
                                if list_i % x == 2:
                                    os.rename(os.path.join(path_name, item), os.path.join(path_name, ((str(num_i)).zfill(y) + '_' + name + '_' + str(
                                        name_num[1]) + last)))  # 第二张命名
                                if list_i % x == 0:
                                    os.rename(os.path.join(path_name, item), os.path.join(path_name, ((str((num_i)-1)).zfill(y) + '_' + name + '_' + str(
                                        name_num[2]) + last)))  # 第三张命名
                                list_i += 1
                                num_i = int(list_i / x) + i
                                pass
                        if x == 4:
                            num_i = i
                            for item in img_list:
                                if list_i % x == 1:
                                    os.rename(os.path.join(path_name, item),
                                              os.path.join(path_name, ((str(num_i)).zfill(y) + '_' + name + '_' + str(
                                                  name_num[0]) + last)))  # 第一张命名
                                if list_i % x == 2:
                                    os.rename(os.path.join(path_name, item), os.path.join(path_name, ((str(num_i)).zfill(y) + '_' + name + '_' + str(name_num[1]) + last)))  # 第二张命名
                                if list_i % x == 3:
                                    os.rename(os.path.join(path_name, item), os.path.join(path_name, ((str(num_i)).zfill(y) + '_' + name + '_' + str(name_num[2]) + last)))  # 第三张命名
                                if list_i % x == 0:
                                    os.rename(os.path.join(path_name, item), os.path.join(path_name, ((str((num_i)-1)).zfill(y) + '_' + name + '_' + str(
                                        name_num[3]) + last)))  # 第四张命名
                                list_i += 1
                                num_i = int(list_i / x) + i
                                pass
                    print('重命名完毕')
                    w2 = True
                    w1 = False
                    chexiao = input("是否需要撤销Y/N")
                    img_new_list = os.listdir(path)
                    if chexiao == 'Y' or chexiao == 'y':
                        for new_item, item in zip(img_new_list, img_original):
                            os.rename(os.path.join(path_name, new_item), os.path.join(path_name, item))
                        print("撤销成功")
                        return True
                    else:
                        break
                except ValueError:
                    print("输入错误，请检查后继续输入")
                    continue
                break
        else:
            print("请检查输入正确序号")
        continue
print("注意事项：撤销选项只可撤销当前次命名，一旦开始继续，不可撤销,路径下可包含其他文件夹\n"
      "A系列支持1-4组命名\n"
      "B系列支持1-4张同一组，以空格区分\n"
      "C系列支持1-4张同一组")
A = 1
rename()
while A:
    selec = input("选择是否继续输入Y/N")
    if selec == 'Y' or selec == 'y':
        rename()
    elif selec == 'N' or selec == 'n':
        A = 0
        print("命名结束")
