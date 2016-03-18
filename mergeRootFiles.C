#include <TFile.h>
#include <TTree.h>
#include <TGraph.h>
#include <TCutG.h>
#include <TCanvas.h>


void mergeRootFiles() {

TChain chain("temps");

chain.Add("----.root");
chain.Add("----.root");
chain.Add("----.root");
chain.Add("----.root");

chain.Merge("------.root");