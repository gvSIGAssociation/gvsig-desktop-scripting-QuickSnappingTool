# encoding: utf-8

import gvsig
from gvsig.libs.formpanel import FormPanel
from gvsig import uselib
from java.awt import BorderLayout
from org.gvsig.scripting.app.extension import ScriptingExtension

from org.gvsig.tools import ToolsLocator

uselib.use_plugin("org.gvsig.snapping.app.mainplugin")
from org.gvsig.app.gui.preferencespage import SnapConfigPage
from javax.swing import JFrame

class QuickSnappingToolExtension(ScriptingExtension):
    def __init__(self):
      pass
  
    def canQueryByAction(self):
      return True
  
    def isEnabled(self,action):
      return gvsig.currentView()!=None
  
    def isVisible(self,action):
      return gvsig.currentView()!=None
      
    def execute(self,actionCommand, *args):
        l = QuickSnappingTool()
        i18n = ToolsLocator.getI18nManager()
        l.showTool(i18n.getTranslation("_Quick_Snapping_Tool"))
        
class QuickSnappingTool(FormPanel):
  def __init__(self):
    FormPanel.__init__(self, gvsig.getResource(__file__, "snappingTool.xml"))
    scp = SnapConfigPage()
    self.pnl1.setLayout(BorderLayout())
    self.pnl1.add(scp)
    self.pnl1.updateUI()

def main(*args):
    l = QuickSnappingTool()
    l.showTool("")