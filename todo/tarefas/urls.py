from django.urls import path
from .views import listarTarefas, listarUsuarios, cadastroAtividade, cadastroUsuario, excluirAtividade, editarAtividade, excluirUsuario, editarUsuario, formLogin, logout_view

urlpatterns = [
    path('listartarefas/', listarTarefas),
    path('listarusuarios/', listarUsuarios),
    path('cadastroatividade/', cadastroAtividade),
    path('cadastrousuario/', cadastroUsuario),
    path('excluirAtividade/<int:id>/', excluirAtividade),
    path('editarAtividade/<int:id>/', editarAtividade),
    path('excluirUsuario/<int:id>/', excluirUsuario),
    path('editarUsuario/<int:id>/', editarUsuario),
    path('login', formLogin),
    path('logout', logout_view),

]