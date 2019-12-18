from . import Loader

#TODO Need to properly type the columns. There are a lot of columns!

class OneQBitLoader(Loader):
    dataset = '1QBIT'
    fileglob = '1QBit_*.csv'

    columns = ['BizDate',
				 'Y',
				 'M',
				 'D',
				 'FuturesProductCode',
				 'OptionsProductCode',
				 'NearbyFuturesSettlementPrice',
				 'NearbyFuturesHighPrice',
				 'NearbyFuturesLowPrice',
				 'NearbyFuturesContractYear',
				 'NearbyFuturesContractMonth',
				 'NearbyFuturesContractVolume',
				 'SecondFuturesSettlementPrice',
				 'SecondFuturesHighPrice',
				 'SecondFuturesLowPrice',
				 'SecondFuturesContractYear',
				 'SecondFuturesContractMonth',
				 'SecondFuturesContractVolume',
				 'TotalFuturesVolume',
				 'RepresentativeImpliedVolatility',
				 'YearofImpliedVolatilityContract',
				 'MonthofImpliedVolatilityContract',
				 'PutOptionVolume',
				 'CallOptionVolume',
				 'TotalOptionVolume',
				 'PutOptionOpenInterest',
				 'CallOptionOpenInterest',
				 'TotalOptionOpenInterest',
				 'NearbyFuturesPreviousDayReferencePrice',
				 'DailyPercentChangeinPrice',
				 'ExcessReturnIndex',
				 'Short-TermSmoothedImpliedVolatility',
				 'Long-TermSmoothedImpliedVolatility',
				 'DailyVarianceProxy',
				 'Short-TermSmoothedHistoricalStandardDeviation',
				 'Long-TermSmoothedHistoricalStandardDeviation',
				 'RatioofShort-TermtoLong-TermSmoothedStandardDeviation',
				 'RatioofShort-TermHISTORICALSTDDEVtoCurrentImpliedVolatility',
				 'HighPricetoLowPriceRatioasPercentSpread',
				 'Short-TermSmoothedHigh-LowPercentageSpread',
				 'Long-TermSmoothedHigh-LowPercentageSpread',
				 'RatioofShort-TermSmoothedtoLong-TermSmoothedHigh-LowPercentageSpread',
				 'Short-TermSmoothedPutOptionVolume',
				 'Long-TermSmoothedPutOptionVolume',
				 'RatioofShort-TermSmoothedtoLong-TermSmoothedPutOptionVolume',
				 'Short-TermSmoothedCallOptionVolume',
				 'Long-TermSmoothedCallOptionVolume',
				 'RatioofShort-TermtoLong-TermSmoothedCallOptionVolume',
				 'RatioofShort-TermSmoothedPutOptionVolumetoShortTermSmoothedCallOptionVolume',
				 'RatioofLong-TermSmoothedPutOptionVolumetoLong-TermSmoothedCallOptionVolume',
				 'PercentageDifferenceShort-TermtoLong-TermRatioofPuttoCallVolume',
				 'Short-TermSmoothedReturnMomentum',
				 'Long-TermSmoothedReturnMomentum',
				 'RatioofShort-TermtoLong-TermSmoothedReturnMomentum',
				 'RatioofShort-TermReturnMomentumtoShort-TermStandardDeviation',
				 'RatioofLong-TermReturnMomentumtoLong-TermStandardDeviation',
				 '20-DayPriceMovingAverage',
				 '60-DayPriceMovingAverage',
				 '200-DayPriceMovingAverage',
				 'PercentageDifferenceCurrentPriceto200-DayMovingAverage',
				 'PercentageDifference20-DayPriceMovingAverageto200-DayPriceMovingAverage',
				 'Peakpriceovertotalperiod',
				 'PeakPriceofNearbyFuturesinLast200Days',
				 '20pctbelowpeakpriceinlast200-businessdays',
				 '20pctabove60-businessdaymovingaverage',
				 'Target1Nearestroundnumberaround20pctabove60-businessdaymovingaverage',
				 'Target2Nearestroundnumberaround20pctbelow60-businessdaymovingaverage',
				 '20pctBelow60-daymovingaverageofpricelevel',
				 'One504-DayStandardDeviationAbovetheMean',
				 'One504-DayStandardDeviationBelowtheMean',
				 'Kurtosis504-DayMovingAverage',
				 'Kurtosis504-DayStandardDeviation',
				 'Skewness504-DayMovingAverage',
				 'Skewness504-DayStandardDeviation',
				 'ProbabilityofRisingAbove20pctabove60-businessdaymovingaverage',
				 'ProbabilityofRisingAboveTarget1(up)',
				 'ProbabilityofFallingBelowTarget2(down)',
				 'ProbabilityofFallingBelow20pctbelow60-businessdaymovingaverage',
				 'MeanofMixtureProbabilityDistribution',
				 'MedianofMixtureProbabilityDistribution',
				 'PrimaryModeofMixtureProbabilityDistribution',
				 'SecondaryModeofMixtureProbabilityDistribution',
				 'SkewofMixtureProbabilityDistribution',
				 'KurtosisofMixtureProbabilityDistribution',
				 'StateofMixtureProbabilityDistribution',
				 'RiskIndex',
				 'OriginforDistribution',
				 'StepsizeforDistribution',
				 'Numberofelementsinthedistributionvector',
				 '-1.00',
				 '-0.99',
				 '-0.98',
				 '-0.97',
				 '-0.96',
				 '-0.95',
				 '-0.94',
				 '-0.93',
				 '-0.92',
				 '-0.91',
				 '-0.90',
				 '-0.89',
				 '-0.88',
				 '-0.87',
				 '-0.86',
				 '-0.85',
				 '-0.84',
				 '-0.83',
				 '-0.82',
				 '-0.81',
				 '-0.80',
				 '-0.79',
				 '-0.78',
				 '-0.77',
				 '-0.76',
				 '-0.75',
				 '-0.74',
				 '-0.73',
				 '-0.72',
				 '-0.71',
				 '-0.70',
				 '-0.69',
				 '-0.68',
				 '-0.67',
				 '-0.66',
				 '-0.65',
				 '-0.64',
				 '-0.63',
				 '-0.62',
				 '-0.61',
				 '-0.60',
				 '-0.59',
				 '-0.58',
				 '-0.57',
				 '-0.56',
				 '-0.55',
				 '-0.54',
				 '-0.53',
				 '-0.52',
				 '-0.51',
				 '-0.50',
				 '-0.49',
				 '-0.48',
				 '-0.47',
				 '-0.46',
				 '-0.45',
				 '-0.44',
				 '-0.43',
				 '-0.42',
				 '-0.41',
				 '-0.40',
				 '-0.39',
				 '-0.38',
				 '-0.37',
				 '-0.36',
				 '-0.35',
				 '-0.34',
				 '-0.33',
				 '-0.32',
				 '-0.31',
				 '-0.30',
				 '-0.29',
				 '-0.28',
				 '-0.27',
				 '-0.26',
				 '-0.25',
				 '-0.24',
				 '-0.23',
				 '-0.22',
				 '-0.21',
				 '-0.20',
				 '-0.19',
				 '-0.18',
				 '-0.17',
				 '-0.16',
				 '-0.15',
				 '-0.14',
				 '-0.13',
				 '-0.12',
				 '-0.11',
				 '-0.10',
				 '-0.09',
				 '-0.08',
				 '-0.07',
				 '-0.06',
				 '-0.05',
				 '-0.04',
				 '-0.03',
				 '-0.02',
				 '-0.01',
				 '0.00',
				 '0.01',
				 '0.02',
				 '0.03',
				 '0.04',
				 '0.05',
				 '0.06',
				 '0.07',
				 '0.08',
				 '0.09',
				 '0.10',
				 '0.11',
				 '0.12',
				 '0.13',
				 '0.14',
				 '0.15',
				 '0.16',
				 '0.17',
				 '0.18',
				 '0.19',
				 '0.20',
				 '0.21',
				 '0.22',
				 '0.23',
				 '0.24',
				 '0.25',
				 '0.26',
				 '0.27',
				 '0.28',
				 '0.29',
				 '0.30',
				 '0.31',
				 '0.32',
				 '0.33',
				 '0.34',
				 '0.35',
				 '0.36',
				 '0.37',
				 '0.38',
				 '0.39',
				 '0.40',
				 '0.41',
				 '0.42',
				 '0.43',
				 '0.44',
				 '0.45',
				 '0.46',
				 '0.47',
				 '0.48',
				 '0.49',
				 '0.50',
				 '0.51',
				 '0.52',
				 '0.53',
				 '0.54',
				 '0.55',
				 '0.56',
				 '0.57',
				 '0.58',
				 '0.59',
				 '0.60',
				 '0.61',
				 '0.62',
				 '0.63',
				 '0.64',
				 '0.65',
				 '0.66',
				 '0.67',
				 '0.68',
				 '0.69',
				 '0.70',
				 '0.71',
				 '0.72',
				 '0.73',
				 '0.74',
				 '0.75',
				 '0.76',
				 '0.77',
				 '0.78',
				 '0.79',
				 '0.80',
				 '0.81',
				 '0.82',
				 '0.83',
				 '0.84',
				 '0.85',
				 '0.86',
				 '0.87',
				 '0.88',
				 '0.89',
				 '0.90',
				 '0.91',
				 '0.92',
				 '0.93',
				 '0.94',
				 '0.95',
				 '0.96',
				 '0.97',
				 '0.98',
				 '0.99',
				 '1.00',
				 '1.01',
				 '1.02',
				 '1.03',
				 '1.04',
				 '1.05',
				 '1.06',
				 '1.07',
				 '1.08',
				 '1.09',
				 '1.10',
				 '1.11',
				 '1.12',
				 '1.13',
				 '1.14',
				 '1.15',
				 '1.16',
				 '1.17',
				 '1.18',
				 '1.19',
				 '1.20',
				 '1.21',
				 '1.22',
				 '1.23',
				 '1.24',
				 '1.25',
				 '1.26',
				 '1.27',
				 '1.28',
				 '1.29',
				 '1.30',
				 '1.31',
				 '1.32',
				 '1.33',
				 '1.34',
				 '1.35',
				 '1.36',
				 '1.37',
				 '1.38',
				 '1.39',
				 '1.40',
				 '1.41',
				 '1.42',
				 '1.43',
				 '1.44',
				 '1.45',
				 '1.46',
				 '1.47',
				 '1.48',
				 '1.49',
				 '1.50',
				 '1.51',
				 '1.52',
				 '1.53',
				 '1.54',
				 '1.55']

    dtypes = {'category': ('FuturesProductCode', 'OptionsProductCode', 'StateofMixtureProbabilityDistribution'),

              'int64': ('Y', 'M', 'D', 'NearbyFuturesContractYear', 'NearbyFuturesContractMonth',
              'NearbyFuturesContractVolume', 'SecondFuturesContractYear',
              'SecondFuturesContractMonth', 'SecondFuturesContractVolume',
              'TotalFuturesVolume', 'YearofImpliedVolatilityContract',
              'MonthofImpliedVolatilityContract', 'PutOptionVolume',
              'CallOptionVolume', 'TotalOptionVolume', 'PutOptionOpenInterest',
              'CallOptionOpenInterest', 'TotalOptionOpenInterest', 'RiskIndex',
              'OriginforDistribution', 'Numberofelementsinthedistributionvector', ),

              'float': ('NearbyFuturesSettlementPrice', 'NearbyFuturesHighPrice', 'NearbyFuturesLowPrice',
                   'SecondFuturesSettlementPrice', 'SecondFuturesHighPrice', 'SecondFuturesLowPrice',
                   'RepresentativeImpliedVolatility', 'NearbyFuturesPreviousDayReferencePrice',
                   'DailyPercentChangeinPrice', 'ExcessReturnIndex', 'Short-TermSmoothedImpliedVolatility',
                   'Long-TermSmoothedImpliedVolatility', 'DailyVarianceProxy', 'Short-TermSmoothedHistoricalStandardDeviation',
                   'Long-TermSmoothedHistoricalStandardDeviation', 'RatioofShort-TermtoLong-TermSmoothedStandardDeviation',
                   'RatioofShort-TermHISTORICALSTDDEVtoCurrentImpliedVolatility', 'HighPricetoLowPriceRatioasPercentSpread',
                   'Short-TermSmoothedHigh-LowPercentageSpread', 'Long-TermSmoothedHigh-LowPercentageSpread',
                   'RatioofShort-TermSmoothedtoLong-TermSmoothedHigh-LowPercentageSpread',
                   'Short-TermSmoothedPutOptionVolume', 'Long-TermSmoothedPutOptionVolume',
                   'RatioofShort-TermSmoothedtoLong-TermSmoothedPutOptionVolume' ,
                   'Short-TermSmoothedCallOptionVolume', 'Long-TermSmoothedCallOptionVolume'
                   'RatioofShort-TermtoLong-TermSmoothedCallOptionVolume',
                   'RatioofShort-TermSmoothedPutOptionVolumetoShortTermSmoothedCallOptionVolume',
                   'RatioofLong-TermSmoothedPutOptionVolumetoLong-TermSmoothedCallOptionVolume',
                   'PercentageDifferenceShort-TermtoLong-TermRatioofPuttoCallVolume', 'Short-TermSmoothedReturnMomentum',
                   'Long-TermSmoothedReturnMomentum', 'RatioofShort-TermtoLong-TermSmoothedReturnMomentum',
                   'RatioofShort-TermReturnMomentumtoShort-TermStandardDeviation',
                   'RatioofLong-TermReturnMomentumtoLong-TermStandardDeviation',
                   '20-DayPriceMovingAverage', '60-DayPriceMovingAverage', '200-DayPriceMovingAverage',
                   'PercentageDifferenceCurrentPriceto200-DayMovingAverage',
                   'PercentageDifference20-DayPriceMovingAverageto200-DayPriceMovingAverage',
                   'Peakpriceovertotalperiod', 'PeakPriceofNearbyFuturesinLast200Days',
                   '20pctbelowpeakpriceinlast200-businessdays', '20pctabove60-businessdaymovingaverage',
                   'Target1Nearestroundnumberaround20pctabove60-businessdaymovingaverage',
                   'Target2Nearestroundnumberaround20pctbelow60-businessdaymovingaverage',
                   '20pctBelow60-daymovingaverageofpricelevel', 'One504-DayStandardDeviationAbovetheMean',
                   'One504-DayStandardDeviationBelowtheMean', 'Kurtosis504-DayMovingAverage',
                   'Kurtosis504-DayStandardDeviation', 'Skewness504-DayMovingAverage',
                   'Skewness504-DayStandardDeviation', 'ProbabilityofRisingAbove20pctabove60-businessdaymovingaverage',
                   'ProbabilityofRisingAboveTarget1(up)', 'ProbabilityofFallingBelowTarget2(down)',
                   'ProbabilityofFallingBelow20pctbelow60-businessdaymovingaverage',
                   'MeanofMixtureProbabilityDistribution', 'MedianofMixtureProbabilityDistribution',
                   'PrimaryModeofMixtureProbabilityDistribution', 'SecondaryModeofMixtureProbabilityDistribution',
                   'SkewofMixtureProbabilityDistribution', 'KurtosisofMixtureProbabilityDistribution',
                   'StepsizeforDistribution', '-1', '-0.99', '-0.98', '-0.97', '-0.96', '-0.95', '-0.94',
                   '-0.93', '-0.92', '-0.91', '-0.9', '-0.89', '-0.88', '-0.87', '-0.86', '-0.85', '-0.84',
                   '-0.83', '-0.82', '-0.81', '-0.8', '-0.79', '-0.78', '-0.77', '-0.76',
                   '-0.75', '-0.74', '-0.73', '-0.72', '-0.71', '-0.7', '-0.69', '-0.68', '-0.67', '-0.66',
                   '-0.65', '-0.64', '-0.63', '-0.62', '-0.61', '-0.6', '-0.59', '-0.58', '-0.57', '-0.56',
                   '-0.55', '-0.54', '-0.53', '-0.52', '-0.51', '-0.5', '-0.49', '-0.48', '-0.47', '-0.46',
                   '-0.45', '-0.44', '-0.43', '-0.42', '-0.41', '-0.4', '-0.39', '-0.38', '-0.37', '-0.36',
                   '-0.35', '-0.34', '-0.33', '-0.32', '-0.31', '-0.3', '-0.29', '-0.28', '-0.27', '-0.26',
                   '-0.25', '-0.24', '-0.23', '-0.22', '-0.21', '-0.2', '-0.19', '-0.18', '-0.17', '-0.16',
                   '-0.15', '-0.14', '-0.13', '-0.12', '-0.11', '-0.1', '-0.09', '-0.08', '-0.07', '-0.06',
                   '-0.05', '-0.04', '-0.03', '-0.02', '-0.01', '0', '0.01', '0.02', '0.03', '0.04', '0.05',
                   '0.06', '0.07', '0.08', '0.09', '0.1', '0.11', '0.12', '0.13', '0.14', '0.15', '0.16',
                   '0.17', '0.18', '0.19', '0.2', '0.21', '0.22', '0.23', '0.24', '0.25', '0.26', '0.27',
                   '0.28', '0.29', '0.3', '0.31', '0.32', '0.33', '0.34', '0.35', '0.36', '0.37', '0.38',
                   '0.39', '0.4', '0.41', '0.42', '0.43', '0.44', '0.45', '0.46', '0.47',
                   '0.48', '0.49', '0.5', '0.51', '0.52', '0.53', '0.54', '0.55', '0.56', '0.57', '0.58',
                   '0.59', '0.6', '0.61', '0.62', '0.63', '0.64', '0.65', '0.66', '0.67', '0.68', '0.69',
                   '0.7', '0.71', '0.72', '0.73', '0.74', '0.75', '0.76', '0.77', '0.78', '0.79', '0.8',
                   '0.81', '0.82', '0.83', '0.84', '0.85', '0.86', '0.87', '0.88', '0.89', '0.9', '0.91',
                   '0.92', '0.93', '0.94', '0.95', '0.96', '0.97', '0.98', '0.99', '1', '1.01', '1.02',
                   '1.03', '1.04', '1.05', '1.06', '1.07', '1.08', '1.09', '1.1', '1.11', '1.12', '1.13',
                   '1.14', '1.15', '1.16', '1.17', '1.18', '1.19', '1.2', '1.21', '1.22', '1.23', '1.24',
                   '1.25', '1.26', '1.27', '1.28', '1.29', '1.3', '1.31', '1.32', '1.33', '1.34', '1.35',
                   '1.36', '1.37', '1.38', '1.39', '1.4', '1.41', '1.42', '1.43', '1.44', '1.45', '1.46',
                   '1.47', '1.48', '1.49', '1.5', '1.51', '1.52', '1.53', '1.54', '1.55',
                    ),

              'date:%Y-%b-%d': ('BizDate')}


oneqbitloader = OneQBitLoader()