# Copyright 2018 ACSONE SA/NV
# License LGPL-3.0 or later (http://www.gnu.org/licenses/lgpl).

{
    "name": "Niki Sulotion",
    "summary": """ """,
    "version": "16.0.1.0.0",
    "license": "LGPL-3",
    "author": "ACSONE SA/NV,Odoo Community Association (OCA)",
    "website": "",
    "depends": ["stock", "crm", "contacts", "website", "portal", "web"],
    "data": [
        "security/ir.model.access.csv",
        "views/moves_history.xml",
        "views/document.xml",
        "views/my_account_documents.xml",
        "views/document_nikki_list_website.xml",
        "views/document_nikki_form_website.xml",
    ],
}
