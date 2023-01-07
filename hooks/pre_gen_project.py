'''
{{ cookiecutter.update({"observability": cookiecutter.observability.split('+') }) }}
{{ cookiecutter.update({"use_sentry": 'sentry' in cookiecutter.observability}) }}
{{ cookiecutter.update({"use_datadog": 'datadog' in cookiecutter.observability}) }}
{{ cookiecutter.update({"use_graylog": 'graylog' in cookiecutter.observability}) }}
{{ cookiecutter.update({"use_prometheus": 'prometheus' in cookiecutter.observability}) }}
'''
