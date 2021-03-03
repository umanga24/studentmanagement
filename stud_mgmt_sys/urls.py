from django.urls import path
from stud_mgmt_sys import views

app_name = 'sms'
urlpatterns = [
    path('list_student/', views.StudentListView.as_view(), name='list_student'),
    path('add_student/', views.StudentAddView.as_view(), name='add_student'),
    path('edit_student/<int:pk>/', views.StudentEditView.as_view(), name= 'edit_student'),
    path('delete_student/<int:pk>', views.StudentDeleteView.as_view(), name='delete_student'),
    path('details_student/<int:pk>', views.StudentDetailsView.as_view(), name = 'details_student'),
    path('list_supervisor/', views.SupervisorListView.as_view(), name = 'list_supervisor'),
    path('add_supervisor/', views.SupervisorAddView.as_view(), name = 'add_supervisor'),
    path('edit_supervisor/<int:pk>/', views.SupervisorEditView.as_view(), name= 'edit_supervisor'),
    path('delete_supervisor/<int:pk>/', views.SupervisorDeleteView.as_view(), name = 'delete_supervisor'),
    path('details_supervisor/<int:pk>/', views.SupervisorDetailsView.as_view(), name = 'details_supervisor'),
    path('list_faculty/', views.FacultyListView.as_view(), name = 'list_faculty'),
    path('add_faculty/', views.FacultyAddView.as_view(), name = 'add_faculty'),
    path('edit_faculty/<int:pk>/', views.FacultyEditView.as_view(), name= 'edit_faculty'),
    path('delete_faculty/<int:pk>/', views.FacultydeleteView.as_view(), name= 'delete_faculty'),
    path('details_faculty/<int:pk>/', views.FacultyDetailsView.as_view(), name= 'details_faculty'),
    path('list_batch/', views.BatchListView.as_view(), name = 'list_batch'),
    path('add_batch/', views.BatchAddView.as_view(), name = 'add_batch'),
    path('edit_batch/<int:pk>/', views.BatchEditView.as_view(), name = 'edit_batch'),
    path('delete_batch/<int:pk>/', views.BatchDeleteView.as_view(), name = 'delete_batch'),
    path('list_section/', views.SectionListView.as_view(), name = 'list_section'),
    path('add_section/', views.SectionAddView.as_view(), name = 'add_section'),
    path('edit_section/<int:pk>/', views.SectioneditView.as_view(), name= 'edit_section'),
    path('delete_section/<int:pk>/', views.SectionDeleteView.as_view(), name='delete_section'),
    path('list_staff/', views.StaffListView.as_view(), name='list_staff'),
    path('add_staff/', views.StaffAddView.as_view(), name='add_staff'),
    path('list_subject/', views.SubjectListView.as_view(), name='list_subject'),
    path('add_subject/', views.SubjectAddView.as_view(), name= 'add_subject'),
    path('list_semester/', views.SemestersListView.as_view(), name='list_semester'),
    path('add_semester/', views.SemestersAddView.as_view(), name='add_semester'),
    path('list_attendance/', views.AttendanceListView.as_view(), name='list_attendance'),
    path('add_attendance/', views.AttendanceAddView.as_view(), name='add_attendance'),
    path('list_attendancereport/', views.AttendanceReportListView.as_view(), name='list_attendancereport'),
    path('add_attendancereport/', views.AttendanceReportAddView.as_view(), name='add_attendancereport'),
    path('login/', views.LoginUserView.as_view(), name = 'login_user'),
    path('logout/', views.LogOutUserView.as_view(), name = 'logout_user'),
    path('register/', views.RegisterUserView.as_view(), name = 'register')


]


