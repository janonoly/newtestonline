from astropy import logger
from django.http import HttpResponseRedirect
from xlrd import open_workbook

import xadmin
from xadmin import views
from .models import CourseList,Question, Paper,PaperList


class CourseListAdmin(object):
    list_display = ['name', 'decs', 'add_time']
    search_fields = ['name', 'decs']
    list_filter = ['name', 'decs', 'add_time']



files=None
class QuestionAdmin(object):

    list_display = ['course','questionType',  'content', 'answer', 'choice_a', 'choice_b',
                    'choice_c', 'choice_d', 'note', 'boolt', 'boolf', 'add_time']
    search_fields = ['course__name','questionType', 'content', 'answer', 'choice_a', 'choice_b',
                     'choice_c', 'choice_d', 'note', 'boolt', 'boolf']
    list_filter = ['course__name','questionType',  'content', 'answer', 'choice_a',
                   'choice_b', 'choice_c', 'choice_d', 'note', 'boolt', 'boolf','add_time']



    import_excel = True
    def post(self, request, *args, **kwargs):
        if 'excel' in request.FILES:
            # 处理逻辑
            execl_file = request.FILES.get('excel')
            files = open_workbook(filename=None, file_contents=request.FILES['excel'].read())

            self.excel_into_model(appname='Exams',model_name='Question', excel_file = files)
            #self.excel_into_model('course', 'Course', excel_file = files)
            #apps.Exams.models.Question.save()
            return HttpResponseRedirect('/xadmin/Exams/question')

        return super(QuestionAdmin, self).post(request, *args, **kwargs)


    def excel_into_model(self,appname, model_name, excel_file):
        # tmp[7].verbose_name.__str__()
        try:

            from django.apps import apps

            #appname_ = get_model(appname, model_name)
            appname_=apps.get_app_config(appname).get_model(model_name)
            fields = appname_._meta.fields
            # 导入model,动态导入
            exec('from %s.models import %s' % (appname, model_name))
        except:
            #logger.info('model_name and appname is not exist')
            print('1')
        field_name = []
        # 只导入第一个sheet中的数据
        table = excel_file.sheet_by_index(0)
        nrows = table.nrows
        table_header = table.row_values(0)
        for cell in table_header:
            for name in fields:
                if cell in name.verbose_name.__str__():
                    field_name.append(name.name)
        if 'add_time' in field_name:
            field_name.remove('add_time')
        for x in range(1, nrows):
            # 行的数据,创建对象,进行报错数据
            exec('obj' + '=%s()' % model_name)
            print(len(field_name))
            for y in range(len(field_name)):
                tempfildname=field_name[y]

                cell_value=table.cell_value(x, y)
                exec('obj1' + '=%s()' % model_name)
                tempstr = 'obj.%s' % field_name[y] + '=cell_value'

                if tempfildname=='course':
                    #exec('obj1' + '=CourseList()')
                    p1 = CourseList.objects.get(name=cell_value)
                    #b1 = Question(course=p1)
                    tempstr='obj.%s' % field_name[y] + '=p1'
                    exec(tempstr)
                    continue
                    #tempstr = 'obj.%s' % field_name[y] + '="%s"' % (p1)
                    #tempstr = 'obj.%s' % tempfildname + '= obj1.objects.get(%s ' % tempfildname + '=%s' % cell_value + '  )'
                # tempstr2 = 'obj.%s' % tempfildname + '= obj.objects.filter(%s ' % tempfildname + ' = %s' % cell_value + '  )'
                # tempstr3 = 'obj.%s' % tempfildname + '= obj.objects.all()'
                # tempstr4 = 'obj.%s' % tempfildname + '= obj.objects.filter()'

                exec(tempstr)
            exec('obj.save()')

class PaperListAdmin(object):
    list_display = ['id','course','name', 'is_allow', 'add_time']
    search_fields = ['id','course', 'name', 'is_allow']
    list_filter = ['id','course__name','name', 'is_allow', 'add_time']

class PaperAdmin(object):
    list_display = ['course', 'paper_name', 'question', 'add_time']
    search_fields = ['course', 'paper_name__name', 'paper_name__id', 'paper_name__is_allow', 'question__id',
                     'question__content', 'question__answer']
    list_filter = ['course__name', 'paper_name', 'question__id', 'question__content','add_time','paper_name__name',]


xadmin.site.register(CourseList, CourseListAdmin)
xadmin.site.register(Question, QuestionAdmin)
xadmin.site.register(PaperList, PaperListAdmin)
xadmin.site.register(Paper, PaperAdmin)