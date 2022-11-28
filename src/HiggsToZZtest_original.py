
import FWCore.ParameterSet.Config as cms

process = cms.Process('TestTest')


process.load('Configuration/StandardSequences/Services_cff')
process.load('FWCore/MessageService/MessageLogger_cfi')

#process.load('HiggsAnalysis/HiggsToZZ4Leptons/hTozzTo4leptonsRunEventFilter_cfi')
#process.hTozzTo4leptonsPath = cms.Path(process.hTozzTo4leptonsRunEventFilter)

#process.load('HiggsAnalysis/HiggsToZZ4Leptons/hTozzTo4leptonsMCGenParticleTreeDrawer_cfi')
#process.hTozzTo4leptonsPath = cms.Path(process.hTozzTo4leptonsMCGenParticleTreeDrawer)

process.printTree1 = cms.EDAnalyzer("ParticleListDrawer",
    src = cms.InputTag("prunedGenParticles"),
    maxEventsToPrint  = cms.untracked.int32(2)
)

#process.printTree2 = cms.EDAnalyzer("ParticleTreeDrawer",
#    src = cms.InputTag("genParticles"),
#    printP4 = cms.untracked.bool(False),
#    printPtEtaPhi = cms.untracked.bool(False),
#    printVertex = cms.untracked.bool(False),
#    printStatus = cms.untracked.bool(False),
#    printIndex  = cms.untracked.bool(False)
#)

process.hTozzTo4leptonsPath = cms.Path(process.printTree1)


# Output definition
process.output = cms.OutputModule("PoolOutputModule",
    fileName = cms.untracked.string('run.root'),
    dataset = cms.untracked.PSet(
        filterName = cms.untracked.string('higgsToZZtest')
    ),
    SelectEvents = cms.untracked.PSet(
        SelectEvents = cms.vstring('hTozzTo4leptonsPath')
    )                               
 )

process.maxEvents = cms.untracked.PSet( input = cms.untracked.int32(10) )

process.source = cms.Source("PoolSource",
   fileNames = cms.untracked.vstring(
#        '/store/mc/PhaseIITDRSpring17MiniAOD/GluGluHToZZTo4L_M125_14TeV_powheg2_JHUgenV702_pythia8/MINIAODSIM/noPU_91X_upgrade2023_realistic_v3-v1/10000/22F18293-F957-E711-A9D2-D485645943AC.root',
#'file:04F13F4C-D358-E711-B4B2-0017A4771048.root'
#'/store/mc/RunIISummer16MiniAODv2/ZZTo4L_13TeV_powheg_pythia8/MINIAODSIM/PUMoriond17_80X_mcRun2_asymptotic_2016_TrancheIV_v6-v1/120000/221CC46F-2FC6-E611-8FFC-0CC47A1E0488.root'
#        'file:/lustre/cms/store/user/defilip/HHTo2b4L/MINIAOD/HHTo2B4L_madgraph_pythia8/crab_Signal_MINIAOD/180103_162918/0000/HHTo2b4L_MINIAOD_Moriond17_100.root'
#'file:/lustre/cms/store/user/taliercio/Twiki/histos4e_25ns/output_ttH_HToZZ_4LFilter_M125_13TeV_powheg2_JHUgenV6_pythia8.root'
 '/store/user/defilip/VBFHH/VBF_HH_CV_1_C2V_1_C3_1_13TeV-madgraph_MINIAOD_100k/VBF_HH_CV_1_C2V_1_C3_1_13TeV-madgraph-GEN_SIM/MINIAOD/210518_150314/0000/HIG_RunIIAutumn18MiniAOD_1.root' 

                            )
                           )


# Endpath
process.o = cms.EndPath ( process.output )
