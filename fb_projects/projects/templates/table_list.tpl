{% extends 'index.tpl' %}

{% block pagecontent %}

    <div class="row">
        <div id="routine_business" style="overflow: auto;">

            <table class="table table-bordered table-striped">
                <thead>
                <tr>
                    <th>ID</th>
                    <th>FB ID</th>
                    <th>Имя</th>
                    <th>Категория</th>
                    <th>email</th>
                </tr>
                </thead>
                <tbody>
                {% for row in projects %}
                    <tr>
                        <td>{{ row.id }}</td>
                        <td>{{ row.fb_id }}</td>
                        <td>{{ row.name }}</td>
                        <td>{{ row.category }}</td>
                        <td editable="true">
                            <a
                                    href="#"
                                    class="editable"
                                    id="{{ row.fb_id }}"
{#                                    csrfmiddlewaretoken="{% csrf_token %}"#}
{#                                    data-type='text'#}
{#                                    data-pk="{{ row.fb_id }}"#}
{#                                    data-params="{#}
{#                                    csrfmiddlewaretoken: {% csrf_token %}#}
{#                                    }"#}
{#                                    data-name='username'#}
{#                                    data-url='/projects/save_mail/'#}
{#                                    data-original-title='Введите почту'#}


                            >{{ row.email }}</a>

                        </td>
                    </tr>
                {% endfor %}
                </tbody>
            </table>
        </div>
    </div>


    <script type="text/javascript">
        $(function () {

            $(document).ready(function () {
                $('tr td').each(function () {
                            if (this.getAttribute('editable') == 'true') {
                                var a = this.getElementsByClassName('editable')[0];
                                var pId = a.getAttribute('id');
                                $('#' + pId).editable(
                                        {
                                            type: 'text',
                                            pk: pId,
                                            name: 'email',
                                            url: '/projects/save_mail/',
                                            title: 'Введите почту'
                                                                        }
                                );
                            }
                        }
                );

            });
        });
    </script>

{% endblock %}