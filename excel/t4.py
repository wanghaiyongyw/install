#coding=utf-8
#/usr/bin/env python
import xlsxwriter,xlrd
import sys,os.path

fname = 'zm6.xlsx'
if not os.path.isfile(fname):
    print u'文件路径不存在'
    sys.exit()
data = xlrd.open_workbook(fname)            # 打开fname文件
data.sheet_names()                          # 获取xls文件中所有sheet的名称
table = data.sheet_by_index(0)              # 通过索引获取xls文件第0个sheet
nrows = table.nrows                         # 获取table工作表总行数
ncols = table.ncols                         # 获取table工作表总列数
workbook = xlsxwriter.Workbook('zm6.xlsx')  #创建一个excel文件
worksheet = workbook.add_worksheet()        #创建一个工作表对象
worksheet.set_column(0,ncols,22)            #设定列的宽度为22像素
#border：边框，align:对齐方式，bg_color：背景颜色，font_size：字体大小，bold：字体加粗
top = workbook.add_format({'border':1,'align':'center','bg_color':'#9999','font_size':13,'bold':True})
green = workbook.add_format({'border':1,'align':'center','bg_color':'green','font_size':12})
yellow = workbook.add_format({'border':1,'bg_color':'yellow','font_size':12})
red = workbook.add_format({'border':1,'align':'center','bg_color':'red','font_size':12})
blank = workbook.add_format({'border':1})
for i in xrange(nrows):
    worksheet.set_row(i,22)                 #设定第i行单元格属性，高度为22像素，行索引从0开始
    for j in  xrange(ncols):
        cell_value = table.cell_value(i,j,) #获取第i行中第j列的值
        if i == 0:
            format = top
        elif i == 3 or i == 6:
            format = blank
        else:
            if j == 0 or j == 2:
                format = yellow
            elif j == 1:
                format = red
            elif j == 3:
                format = green
                green.set_num_format('yyyy-mm-dd')  #设置时间格式
        worksheet.write(i,j,cell_value,format)      #把获取到的值写入文件对应的行列
        format.set_align('vcenter')                 #设置单元格垂直对齐
workbook.close()