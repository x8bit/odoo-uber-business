{
	'name': "X8 Uber Business Empleados",
	'version': '1.0.0',
	'author': "X8BIT SA DE CV",
	'website': 'www.x8bit.com',
	'category': 'Specific Industry Applications',
	'application': False,
	'description': """
	X8 Uber Business Empleados - Módulo de administración de empleados que pueden usar Uber Business

		- Administración de lista de empleados que usan Uber.
	""",
	'data': [
		'views/menu.xml',
		'views/empleado_form_view.xml',
		'views/empleados_uber_view.xml'
	],
	'depends': [
		'base',
		'hr'
	],
}