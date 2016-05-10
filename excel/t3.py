# __author__ = 'wanghaiyong'
#-*- encoding:utf-8 -*-
import xlsxwriter as wx
workbook = wx.Workbook('hello.xlsx')


workbook.add_format({'bold': 1,'border': 1,'align': 'center','valign': 'vcenter'})
worksheet = workbook.add_worksheet()

worksheet.set_column('A:A', len('hello world')+1)
worksheet.write(0, 2, 'hello world')
worksheet.merge_range('A1:E1',u'')
workbook.close()


#self.worksheet.merge_range('I7:L7',u'',self.cell_ff)