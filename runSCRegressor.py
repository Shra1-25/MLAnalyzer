import os

cfg='RecHitAnalyzer/python/SCRegressor_cfg.py'
#inputFiles_='file:../step_full.root'
#inputFiles_='file:/eos/uscms/store/user/mba2012/FEVTDEBUG/h24gamma_1j_1M_100MeV_noPU_FEVTDEBUG/180109_233954/0000/step_full_1.root'
#inputFiles_='file:/eos/uscms/store/user/mba2012/AODSIM/SinglePi0Pt60_pythia8_2016_25ns_Moriond17MC_PoissonOOTPU_AODSIM_m000/180413_215734/0000/step_full_1.root'
#inputFiles_='file:/eos/uscms/store/user/mba2012/AODSIM/SinglePi0Pt60_pythia8_2016_25ns_Moriond17MC_PoissonOOTPU_AODSIM_m100/180413_215901/0000/step_full_1.root'
#inputFiles_='file:/eos/uscms/store/user/mba2012/AODSIM/SinglePi0Pt60_pythia8_2016_25ns_Moriond17MC_PoissonOOTPU_AODSIM_m000/180416_105657/0000/step_full_1.root'
#inputFiles_='file:/eos/uscms/store/user/mba2012/AODSIM/DoublePi0Pt30To90_pythia8_m000_2016_25ns_Moriond17MC_PoissonOOTPU_AODSIM/180604_160025/0004/step_full_4917.root'
#inputFiles_='file:/eos/uscms/store/user/mba2012/AODSIM/DoublePi0Pt50To60_m0To1600_pythia8_2016_25ns_Moriond17MC_PoissonOOTPU_AODSIM/180620_123051/0000/step_full_filtered_1.root'
#inputFiles_='file:/eos/uscms/store/user/mba2012/AODSIM/DoublePi0Pt50To60_m000_pythia8_2016_25ns_Moriond17MC_PoissonOOTPU_AODSIM/180622_100748/0000/step_full_1.root'
#inputFiles_='file:/eos/uscms/store/user/mba2012/AODSIM/SinglePi0Pt60_pythia8_2016_25ns_Moriond17MC_PoissonOOTPU_AODSIM_m600/180611_092217/0000/step_full_1.root'
#inputFiles_='/store/user/lpcml/mandrews/AODSIM/DoublePi0Pt30To50_m0To1600_pythia8_2016_25ns_Moriond17MC_PoissonOOTPU_AODSIM/180917_151524/0000/step_full_1.root'
#inputFiles_='/store/user/lpcml/mandrews/AODSIM/DoublePi0Pt15To100_m0To1600_pythia8_2016_25ns_Moriond17MC_PoissonOOTPU_AODSIM/181212_004828/0000/step_full_1.root'
#inputFiles_='/store/user/lpcml/mandrews/AODSIM/DoublePi0Pt15To100_m0To1600_pythia8_noPU_AODSIM/190116_160039/0000/step_full_1.root'
#inputFiles_='/store/user/lpcml/mandrews/AODSIM/DoublePhotonPt15To100_pythia8_noPU_AODSIM/190219_231402/0000/step_full_1.root'
#inputFiles_='/store/user/lpcml/mandrews/AODSIM/DoublePi0Pt15To100_m000_pythia8_noPU_AODSIM/190220_040632/0000/step_full_1.root'
#inputFiles_='/store/user/lpcml/mandrews/AODSIM/SM2gamma_1j_1M_2016_25ns_Moriond17MC_PoissonOOTPU_AODSIM/180904_071354/0000/step_full_1.root'
#inputFiles_='/store/user/lpcml/mandrews/AODSIM/DoublePi0Pt15To100_m0To1600_pythia8_noPU_AODSIM_mlog_ptexp/190217_185619/0000/step_full_1.root'
#inputFiles_='/store/mc/RunIIFall17MiniAODv2/DiPhotonJets_MGG-80toInf_13TeV_amcatnloFXFX_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/100000/72CD8425-3B87-E811-AEA5-24BE05CEADA1.root'
#inputFiles_='/store/mc/RunIIFall17MiniAODv2/GluGluHToGG_M125_13TeV_amcatnloFXFX_pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/BC2864DE-5B42-E811-9C51-0025905A6138.root'
#inputFiles_='/store/mc/RunIIFall17MiniAODv2/DYToEE_M-50_NNPDF31_13TeV-powheg-pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/10000/544FA228-5845-E811-A88A-782BCB539B14.root'
#inputFiles_='/store/mc/RunIIFall17MiniAODv2/GJet_Pt-20to40_DoubleEMEnriched_MGG-80toInf_TuneCP5_13TeV_Pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/00000/288ED03F-6C42-E811-96EC-0CC47A4C8E98.root'
#inputFiles_='/store/mc/RunIIFall17MiniAODv2/QCD_Pt-30toInf_DoubleEMEnriched_MGG-40to80_TuneCP5_13TeV_Pythia8/MINIAODSIM/PU2017_12Apr2018_94X_mc2017_realistic_v14-v1/90000/FEE7EA67-5942-E811-9C25-0CC47A4D75EE.root'
#inputFiles_='/store/data/Run2017B/DoubleEG/MINIAOD/31Mar2018-v1/80000/FAC7DC8A-3737-E811-8BA7-6CC2173DC380.root'
#inputFiles_='/store/user/lpcml/mandrews/AODSIM/h24gamma_1j_1M_100MeV_2016_25ns_Moriond17MC_PoissonOOTPU_AODSIM/180903_152402/0000/step_full_1.root'
#inputFiles_='/store/user/lpcml/mandrews/AODSIM/h24gamma_1j_1M_400MeV_2016_25ns_Moriond17MC_PoissonOOTPU_AODSIM/180908_013040/0000/step_full_1.root'
#inputFiles_='/store/user/lpcml/mandrews/AODSIM/h24gamma_1j_1M_1GeV_2016_25ns_Moriond17MC_PoissonOOTPU_AODSIM/180902_213131/0000/step_full_1.root'
inputFiles_='/store/user/lpcml/mandrews/MINIAODSIM/h24gamma_1j_1M_100MeV_PU2017_MINIAODSIM/190409_144816/0000/step_miniaodsim_1.root'
#inputFiles_='/store/user/lpcml/mandrews/MINIAODSIM/h24gamma_1j_1M_200MeV_PU2017_MINIAODSIM/190410_034928/0000/step_miniaodsim_1.root'
#inputFiles_='/store/user/lpcml/mandrews/MINIAODSIM/h24gamma_1j_1M_400MeV_PU2017_MINIAODSIM/190410_035004/0000/step_miniaodsim_1.root'
#inputFiles_='/store/user/lpcml/mandrews/MINIAODSIM/h24gamma_1j_1M_1GeV_PU2017_MINIAODSIM/190410_034853/0000/step_miniaodsim_1.root'
#inputFiles_='file:step_full_filtered.root'
#inputFiles_='root://cmseos.fnal.gov/%s'%inputFiles_
#root://cmsxrootd-site.fnal.gov

maxEvents_=-1
maxEvents_=1000
skipEvents_=0
#outputFile_='output.root'
#inputTag=inputFiles_.strip('file:').strip('_FEVTDEBUG.root')
#inputTag='TEST'

#cmd="cmsRun %s inputFiles=%s maxEvents=%d skipEvents=%d outputFile=%s"%(cfg,inputFiles_,maxEvents_,skipEvents_,outputFile_)
#for ievt in range(1):
#if not os.path.isdir(inputTag):
#    os.system('mkdir %s'%(inputTag))
#cmd="cmsRun %s inputFiles=%s maxEvents=%d skipEvents=%d"%(cfg,inputFiles_,maxEvents_,ievt)
cmd="cmsRun %s inputFiles=%s maxEvents=%d skipEvents=%d"%(cfg,inputFiles_,maxEvents_,skipEvents_)
print '%s'%cmd
os.system(cmd)
#os.system('mv c*.eps %s/'%(inputTag))
#    os.system('mv cEB*_%d.eps %s/'%(ievt+1,inputTag))

#os.system('scram b -j8')
