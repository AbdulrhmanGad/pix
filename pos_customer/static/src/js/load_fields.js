/** @odoo-modul */
odoo.define('pos_customer.load_fields', function (require) {
    "use strict";

const { PosGlobalState } = require('point_of_sale.models');
const Registries = require('point_of_sale.Registries');

const GenderPosGlobalState = (PosGlobalState) => class GenderPosGlobalState extends PosGlobalState {
    async _processData(loadedData) {

   await super._processData(...arguments);

   this.gender = loadedData['res.partner'];
   console.log(this.gender)
  }
}
Registries.Model.extend(PosGlobalState, GenderPosGlobalState)

});