#used by render_doc

def mktitle(context, doc_type):
    title = ''
    if doc_type == 'proj_brief':
        title = "ES_Project_Briefs_01.29.2024.docx" #Improvement: add auto date
        
    # if doc_type == 'pricing':
    #     title = f"{context['subscriber_underscore']}_Pricing_Estimate_{context['app_title_underscore']}.docx"
    # if doc_type == 'maint_enh': 
    #     title = f"{context['subscriber_underscore']}_Maintenance_Enhancement_Details_{context['app_title_underscore']}.docx"
    # if doc_type == 'maint':
    #     title = f"{context['subscriber_underscore']}_Maintenance_Details_{context['app_title_underscore']}.docx"
    # if doc_type == 'poc':
    #     title = f"{context['subscriber_underscore']}_POC_{context['app_title_underscore']}.docx"
    # if doc_type == 'design_poc':
    #     title = f"{context['subscriber_underscore']}_Design_POC_{context['app_title_underscore']}.docx"
    # if doc_type == 'tech_req':
    #     title = f"{context['subscriber_underscore']}_Requirements_Doc_{context['app_title_underscore']}.docx"
    # if doc_type == 're':
    #     title = f"{context['subscriber_underscore']}_Rough_Estimate_Doc_{context['app_title_underscore']}.docx"
    return title