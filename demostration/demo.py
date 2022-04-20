from PyVoltammetry import analyse, visualisation

# For data analysing
cv = analyse.AnalyseCV()

# Import data from string variables or txt file
# cv.ImportData(data_str='')
cv.ImportDataFromTxt('Example-Pt_CV.txt')

# Fitting the double layer with two linear functions
DL_func_lower, DL_func_upper = cv.FittingDoubleLayer(doubleLayer_range=(0.4,0.5))

# Extract the data of Pt-H or Pt-O peak
Data_H = cv.ExtractPeaks(peak='H')
Data_O = cv.ExtractPeaks(peak='O')

# Calculate the peak area
area_O = cv.CalcuatePeakArea(scan_rate=0.02, peak='H')
area_H = cv.CalcuatePeakArea(scan_rate=0.02, peak='O')

# For result demostration
figure = visualisation.ShowFigure(cv)

# Customise the figure
figure.AddRawData()
figure.AddDoubleLayer()
figure.FillPeak(peak='O')

# show figure
figure.Show()
# export figure to bytes
img_bytes = figure.ExportToBytes()

figure.Close()