# encoding: utf-8

import gvsig
from gvsig.libs.formpanel import FormPanel
from gvsig import uselib
from java.awt import BorderLayout
from java.awt.event import ComponentAdapter
from org.gvsig.scripting.app.extension import ScriptingExtension

from org.gvsig.tools import ToolsLocator
from org.gvsig.tools.swing.api import ToolsSwingLocator

uselib.use_plugin("org.gvsig.snapping.app.mainplugin")
from org.gvsig.app.gui.preferencespage import SnapConfigPage
from org.gvsig.app.project.documents.view.gui import ViewSnappingInfoImpl

from javax.swing import JFrame

class ClosePanelListener(ComponentAdapter):
    def __init__(self,extension):
      self.extension = extension

    def componentHidden(self, e):
      self.extension.panel = None

class QuickSnappingToolExtension(ScriptingExtension):
    def __init__(self):
      self.panel = None
      pass
  
    def canQueryByAction(self):
      return True
  
    def isEnabled(self,action):
      currentView = gvsig.currentView()
      if self.panel != None:
        self.panel.setView(currentView)
      return currentView!=None
  
    def isVisible(self,action):
      return gvsig.currentView()!=None
      
    def execute(self,actionCommand, *args):
      if self.panel == None:
          self.panel = QuickSnappingTool()
          self.panel.asJComponent().addComponentListener(ClosePanelListener(self))
          i18n = ToolsLocator.getI18nManager()
          self.panel.showTool(i18n.getTranslation("_Quick_Snapping_Tool"))
        
class QuickSnappingTool(FormPanel):
  def __init__(self):
    FormPanel.__init__(self, gvsig.getResource(__file__, "snappingTool.xml"))
    self.scp = SnapConfigPage()
    self.pnl1.setLayout(BorderLayout())
    self.pnl1.add(self.scp)
    self.pnl1.updateUI()

    self.vsi = ViewSnappingInfoImpl()
    currentView = gvsig.currentView()
    if currentView != None:
      self.vsi.setMapContext(currentView.getMapContext());
    self.pnlLayers.setLayout(BorderLayout())
    self.pnlLayers.add(self.vsi)
    self.pnlLayers.updateUI()
    
    toolsSwingManager = ToolsSwingLocator.getToolsSwingManager()
    toolsSwingManager.translate(self.tbdTabs)
    toolsSwingManager.translate(self.btnSave)
    toolsSwingManager.translate(self.btnClose)
    
  def btnSave_click(self,args):
    self.scp.storeValues()
    self.vsi.applyChanges()

  def setView(self, view):
    if view != None:
      self.vsi.setMapContext(view.getMapContext());
    

def main(*args):
    l = QuickSnappingTool()
    l.showTool("")