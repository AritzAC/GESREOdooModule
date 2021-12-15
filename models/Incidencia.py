# To change this license header, choose License Headers in Project Properties.
# To change this template file, choose Tools | Templates
# and open the template in the editor.

class Incidencia(models.Model):
    _name = 'gesre.Incidencias'
    
    estrellas = fields.Integer(String="Estrellas", required="false")
    horas = fields.Integer(String="Horas", required="false")
    precio = fields.Double(String="Precio", required="false")
    
    tipoIncidencia = fields.Selection([('a', 'ELECTRICO'),
                                      ('b', 'FACHADA'),
                                      ('c', 'FONTANERIA'),
                                      ('d', 'GAS'),
                                      ('e', 'HUMEDAD'),
                                      ('f', 'CERRAJERO'),
                                      ('g', 'REVISION')], string="Tipo Incidencia", required="true")
    
    statusIncidencia = fields.Selection([('a', 'PENDIENTE'),
                                        ('b', 'PROCESO'),
                                        ('c', 'CERRADO')], string="Estado de Incidencia", required="true")                                  
   