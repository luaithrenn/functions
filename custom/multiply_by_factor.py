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
        Multiply an input data items by a constant to produce a data output item.
        '''
    
    def __init__(self, input_item, factor, output_item):
        self.input_item = input_item
        self.output_item = output_item
        self.factor = float(factor)
        super().__init__()
    
    def execute(self, df):
        df = df.copy()
        df[self.output_item] = df[input_item] * self.factor
        return df
    
    @classmethod
    def build_ui(cls):
        # define arguments that behave as function inputs
        inputs = []
        inputs.append(ui.UIMultiItem(
          name='input_item',
          datatype=float,
          description="Data item to adjusta",
        ))
        inputs.append(ui.UISingle(
          name='factor',
          datatype=float
        ))
        outputs = []
        outputs.append(ui.UIFunctionOutSingle(
          name='output_item',
           datatype=float,
           description='Adjusted item'
         ))
        return (inputs, outputs)
