from __future__ import print_function
import sys, os
sys.path.insert(1,"../../")
import h2o
from tests import pyunit_utils
from h2o.utils.typechecks import assert_is_type
from h2o.assembly import *
from h2o.transforms.preprocessing import *

def h2oassembly_to_pojo():
  """
  Python API test: H2OAssembly.to_pojo(pojo_name=u'', path=u'', get_jar=True)

  Copied from pyunit_assembly_demo.py
  """

  fr = h2o.import_file(pyunit_utils.locate("smalldata/iris/iris_wheader.csv"), col_types=["numeric","numeric","numeric","numeric","string"])  # import data
  assembly = H2OAssembly(steps=[("col_select",      H2OColSelect(["sepal_len", "petal_len", "class"])),                                # col selection
                                ("cos_sep_len",     H2OColOp(op=H2OFrame.cos, col="sepal_len", inplace=True)),                         # math operation
                                ("str_cnt_species", H2OColOp(op=H2OFrame.countmatches, col="class", inplace=False, pattern="s"))])     # string operation

  result = assembly.fit(fr)  # fit the assembly

  try:
      results_dir = pyunit_utils.locate("results")    # find directory path to results folder
      assembly.to_pojo(pojo_name="iris_munge", path=results_dir, get_jar=True)
      assert os.path.isfile(os.path.join(results_dir, "h2o-genmodel.jar")), "H2OAssembly.to_pojo() " \
                                                                            "command is not working."
  except Exception as e:
      if 'File not found' in e.args[0]:
        assembly.to_pojo(pojo_name="iris_munge", path='', get_jar=False)  # just print pojo to screen if directory does not exists
      else:
        assert False, "H2OAssembly.to_pojo() command is not working."



if __name__ == "__main__":
    pyunit_utils.standalone_test(h2oassembly_to_pojo)
else:
    h2oassembly_to_pojo()
