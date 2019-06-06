import inspect
import logging
import datetime as dt
import math
from sqlalchemy.sql.sqltypes import TIMESTAMP,VARCHAR
import numpy as np
import pandas as pd

from iotfunctions.base import BaseTransformer
from iotfunctions import ui

logger = logging.getLogger(__name__)


# Specify the URL to your package here.
# This URL must be accessible via pip install

PACKAGE_URL = 'git+https://github.com/luaithrenn/functions@'

class MultiplyByFactor(BaseTransformer):
    
    '''
    Multiply input items by a factor to produce a result
    '''
    
    def __init__(self, input_items, factor, output_items):
        #Initalization method.  Define input and output items here.
        
        self.input_items = input_items
        self.output_items = output_items
        self.factor = factor
        super().__init__()
    
    def execute(self, df):
        #Execute method.
        
        df = df.copy()
        for i,input_item in enumerate(self.input_items):
            df[self.output_items[i]] = df[input_item] * self.factor
        return df

    @classmethod
    def build_ui(cls):
        #define arguments that behave as function inputs
        inputs = []
        inputs.append(ui.UISingleItem(
          name='input_item_1',
          datatype=float,
          description='Input item 1'
          ))
        inputs.append(ui.UISingleItem(
          name='factor',
          datatype=float,
          description="Factor"
          ))
        outputs = []
        outputs.append(ui.UIFunctionOutSingle(
            name='output_item',
            datatype=float,
            description='Result of multiplication'
            ))
        return (inputs,outputs)







