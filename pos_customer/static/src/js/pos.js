odoo.define('pos_customer.pos', function (require) {
"use strict";

    const { getDataURLFromFile } = require("web.utils");
    const PosComponent = require("point_of_sale.PosComponent");
    const Registries = require("point_of_sale.Registries");

    const { onMounted, useState, onWillUnmount } = owl;

    class PartnerEdit extends PosComponent {
        setup() {
            super.setup();
            
            const partner = this.props.partner;
            this.changes = useState({
                gender: partner.gender || "",
                customerid: partner.customerid || "",

            });

            onMounted(() => {
                this.env.bus.on("save-partner", this, this.saveChanges);
            });

            onWillUnmount(() => {
                this.env.bus.off("save-partner", this);
            });
        }


        // NOTE: this functions was kept for compatibility with stable
        

}
    PartnerEdit.template = "PartnerEdit";

    Registries.Component.add(PartnerEdit);
    return PartnerEdit;


});