"Bar chart with table"

from reportlab.graphics.shapes import Drawing, _DrawingEditorMixin
from reportlab.lib.colors import PCMYKColor, black
from reportlab.graphics.charts.barcharts import VerticalBarChart
from reportlab.graphics.widgets.table import TableWidget
from reportlab.graphics.charts.legends import Legend
from reportlab.lib.validators import Auto
from reportlab.lib import colors
import random


class BarChart(_DrawingEditorMixin, Drawing):
    """
    Chart Features
    """

    def __init__(self, width=403, height=163, *args, **kwargs):
        """
        BarChar constructor
        """

        # Configuration
        Drawing.__init__(self, width, height, *args, **kwargs)

        self.width = 400
        self.height = 200

        self.create_graphic()

        self.insert_legend()

        self.create_table()

    def create_graphic(self):
        """
        Create a graphic.
        """

        self._add(self, VerticalBarChart(), name='chart')

        self.chart.data = [
            [4], [3], [1], [2]
        ]

        self.chart.x             = 140
        self.chart.y             = 75
        self.chart.height        = 73
        self.chart.width         = 250

        self.chart.fillColor            = None
        self.chart.barWidth             = 2
        self.chart.groupSpacing         = 5
        self.chart.barSpacing           = 0.5
        self.chart.bars.strokeWidth     = 0.5
        self.chart.bars.strokeColor     = PCMYKColor(0,0,0,100)

        # Vertical axes
        self.chart.valueAxis.labels.fontName        = 'Helvetica'
        self.chart.valueAxis.labels.fontSize        = 5
        self.chart.valueAxis.visibleGrid            = False
        self.chart.valueAxis.visibleTicks           = False
        self.chart.valueAxis.valueMin               = 0
        self.chart.valueAxis.valueMax               = 4
        self.chart.valueAxis.valueStep              = 1

        # Horizontal axes
        self.chart.categoryAxis.strokeWidth         = 0.25
        self.chart.categoryAxis.visibleGrid         = False
        self.chart.categoryAxis.visibleTicks        = False
        self.chart.categoryAxis.labels.boxAnchor    = 'e'
        self.chart.categoryAxis.labels.fontSize     = 8
        self.chart.categoryAxis.categoryNames       = ['Questões']

    def random_color(self):
        """
        Get a random color.
        """

        value = lambda: random.randint(0, 100)

        return PCMYKColor(value(), value(), value(), value(), alpha=100)

    def insert_legend(self):
        """
        Insert legend into graphic
        """

        self._add(self, Legend(), name='legend')

        self.legend.deltay           = 8
        self.legend.fontName         = 'Helvetica'
        self.legend.fontSize         = 5
        self.legend.strokeWidth      = 0.5
        self.legend.strokeColor      = PCMYKColor(0,0,0,100)
        self.legend.alignment        = 'right'
        self.legend.columnMaximum    = 3
        self.legend.boxAnchor        = 'sw'
        self.legend.y                = 75
        self.legend.x                = 24
        self.legend.dx               = 8
        self.legend.dy               = 5
        self.legend.dxTextSpace      = 5
        self.legend.deltax           = 0
        self.legend.colorNamePairs   = Auto(obj=self.chart)

        self.chart.bars[0].fillColor = self.random_color()
        self.chart.bars[1].fillColor = self.random_color()
        self.chart.bars[2].fillColor = self.random_color()
        self.chart.bars[3].fillColor = self.random_color()

    def create_table(self):
        """
        Create a table in PDF.
        """

        self._add(self, TableWidget(), name='table')

        self.table.data = [
            ['Q1', 'Questão 01', '4 Pontos'],
            ['Q2', 'Questão 02', '3 Pontos'],
            ['Q3', 'Questão 03', '1 Pontos'],
            ['Q4', 'Questão 04', '2 Pontos']
        ]

        for i in range(len(self.chart.data)):
            self.chart.bars[i].name = self.table.data[i][0]

        self.table.height                       = 45
        self.table.borderStrokeColor            = PCMYKColor(0, 12, 24, 36)
        self.table.fillColor                    = PCMYKColor(0, 3, 7, 6)
        self.table.borderStrokeWidth            = 0.5
        self.table.horizontalDividerStrokeColor = PCMYKColor(0, 12, 24, 36)
        self.table.verticalDividerStrokeColor   = colors.black
        self.table.horizontalDividerStrokeWidth = 0.5
        self.table.verticalDividerStrokeWidth   = 0.5
        self.table.fontName                     = 'Times-Bold'
        self.table.fontSize                     = 7
        self.table.fontColor                    = colors.black
        self.table.alignment                    = 'left'
        self.table.width                        = 380

if __name__ == "__main__":
    BarChart().save(formats=['pdf'], outDir='.', fnRoot=None)
