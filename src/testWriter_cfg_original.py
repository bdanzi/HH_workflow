#!/usr/bin/env cmsRun
import FWCore.ParameterSet.Config as cms

process = cms.Process("Writer")

process.maxEvents = cms.untracked.PSet(input = cms.untracked.int32(-1))

process.source = cms.Source("PoolSource",
	fileNames = cms.untracked.vstring('file:/lustre/home/nicola/8F5DE832-A1A9-334B-B931-A5D2B8CB61F5.root')
)

process.load("FWCore.MessageService.MessageLogger_cfi")
process.MessageLogger.cerr.threshold = 'INFO'

process.writer = cms.EDAnalyzer("LHEWriter",
	moduleLabel = cms.untracked.InputTag("externalLHEProducer")
)


process.outpath = cms.EndPath(process.writer)
