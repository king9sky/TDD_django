#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Author  : Marvin King
# Date     : 2019-02-22
from .base import FunctionalTest

class ItemValidationTest(FunctionalTest):


    def can_not_add_empty_list_items(self):
        # 乔伊访问首页，不小心提交一个空待办事项
        # 输入框中没输入内容，她就按下了回车

        # 首页刷新了，显示了一个错误信息
        # 提示待办事项不能为空

        # 她输入了一些文字，然后再次提交，这次没有问题了

        # 她有点儿调皮，又提交了一个空待办事项

        # 在清单页她看到了一个类似的错误消息

        # 输入文字之后就没问题了
        self.fail('wirte me!')
