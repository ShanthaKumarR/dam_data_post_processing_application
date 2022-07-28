from UI.postProcessing import DataPostProcessingModels
from seasave_data_post_processing.data_post_processing import Data_post_processing
from controller.controller import DataPostProcessingController
from view.view import View

class data_post_processing_app:
    
    def __init__(self) -> None:
        self.view = View() 
        model_table = self.view.ui.DP_TableView
        dpc_template_CB = self.view.ui.DP_model_temp_CB
        DP_SEBbatchLE= self.view.ui.DP_SEBbatchLE
        data_post_processing_model_obj = DataPostProcessingModels()
        data_post_processing_backend_obj = Data_post_processing()
        controls = self.view.ui_controls
        self.controller_obj = DataPostProcessingController(model_table, controls, data_post_processing_model_obj, data_post_processing_backend_obj, dpc_template_CB, DP_SEBbatchLE)
        self.view.start_app()

if __name__ == '__main__':
    window = data_post_processing_app()   
    