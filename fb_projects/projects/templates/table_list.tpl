{% extends 'index.tpl' %}

{#{% block pagetitle %}#}
{#    Dashboard#}
{#{% endblock %}#}


{% block pagecontent %}
    <div class="row">
        <div id="routine_business" style="overflow: auto;">

            <table class="table table-bordered table-striped">
                <thead>
                <tr>
                    <th>ID</th>
                    <th>Домен</th>
                    <th>Еиейл</th>
                    <th>Ссылка FB</th>
                    <th>Дата заведения</th>
                </tr>
                </thead>
                <tbody>
                {% for row in projects %}
                    <tr>
                        <td>{{ row.id }}</td>
                        <td>{{ row.domain }}</td>
                        <td>{{ row.email }}</td>
                        <td>{{ row.url_fb }}</td>
                        <td>{{ row.date_create }}</td>
                    </tr>
                {% endfor %}
                </tbody>
            </table>
        </div>

{% endblock %}