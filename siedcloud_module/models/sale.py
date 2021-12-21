from odoo import models, fields, api


class Sale(models.Model):
     _name = 'sale'

     customer_id = fields.Many2one(comodel_name="customer", string="Cliente", required=True)
     product_ids = fields.Many2many("product", string="Productos")
     state = fields.Selection([('pending','Pendiente'),('finalized','Finalizada'),('deployed','Deployado')])
     cloud = fields.Selection([('google','Google Cloud'),('azure','Azure'),('amazon','Amazon'),('siedcloud','SiedCloud')], default='siedcloud', required=True)
     pipeline = fields.Text(string="Pipeline", compute="_generate_deploy")


     @api.depends('cloud')
     def _generate_deploy(self):
          #self.pipeline = 'Deploy services to => "' + self.cloud + '" | For customer => ' + str(self.customer_id.id) + ' | With service owner name => "' + self.customer_id.name + '"'
          self.pipeline = """
          - task: {}-pipelines-tasks-terraform-cli.TerraformCLI@0
               displayName: 'Run terraform plan for ID =>{} | User => {}'
               inputs:
                    command: deploy-plan
                    workingDirectory: $(terraformWorkingDirectory)
                    environmentServiceName: $(serviceConnection)
                    commandOptions: -var location=$(cloudLocation)
                    """.format(self.cloud, str(self.customer_id.id), self.customer_id.name)

     def boton_finalizar(self):
          self.state = "finalized"
     
     def boton_deploy(self):
          self.state = "deployed"
