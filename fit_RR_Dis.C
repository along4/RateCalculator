
#include "TCanvas.h"
#include "TTree.h"
#include "TH1D.h"
#include "TRandom.h"
#include <iomanip>

using namespace std;



void fit_RR_Dis(){


	TString fileString = "./30S+a/calcRate/30S4He_new.root";
	Double_t quant[7];
    Double_t quantPosition[7] = {0.01,0.025,0.16,0.5,0.84,0.975,1.0};

	TFile *rootFile = new TFile(fileString);
	TTree *TEMPS = (TTree*)rootFile->Get("temps");

	TCanvas *c1 = new TCanvas("c1","Title is gonna Title");
	c1->Divide(4,6);


	c1->cd(1);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0010");
	TH1F *h1 = (TH1F*)gPad->GetPrimitive("htemp");
	h1->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "0.10" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;


	c1->cd(2);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0015");
	TH1F *h2 = (TH1F*)gPad->GetPrimitive("htemp");
	h2->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "0.15" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;


	c1->cd(3);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0020");
	TH1F *h3 = (TH1F*)gPad->GetPrimitive("htemp");
	h3->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "0.20" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(4);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0030");
	TH1F *h4 = (TH1F*)gPad->GetPrimitive("htemp");
	h4->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "0.30" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(5);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0040");
	TH1F *h5 = (TH1F*)gPad->GetPrimitive("htemp");
	h5->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "0.40" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(6);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0050");
	TH1F *h6 = (TH1F*)gPad->GetPrimitive("htemp");
	h6->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "0.50" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(7);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0060");
	TH1F *h7 = (TH1F*)gPad->GetPrimitive("htemp");
	h7->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "0.60" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(8);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0070");
	TH1F *h8 = (TH1F*)gPad->GetPrimitive("htemp");
	h8->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "0.70" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(9);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0080");
	TH1F *h9 = (TH1F*)gPad->GetPrimitive("htemp");
	h9->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "0.80" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(10);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0090");
	TH1F *h10 = (TH1F*)gPad->GetPrimitive("htemp");
	h10->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "0.90" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(11);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0100");
	TH1F *h11 = (TH1F*)gPad->GetPrimitive("htemp");
	h11->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "1.00" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(12);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0150");
	TH1F *h12 = (TH1F*)gPad->GetPrimitive("htemp");
	h12->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "1.50" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(13);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0200");
	TH1F *h13 = (TH1F*)gPad->GetPrimitive("htemp");
	h13->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "2.00" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(14);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0250");
	TH1F *h14 = (TH1F*)gPad->GetPrimitive("htemp");
	h14->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "2.50" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(15);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0300");
	TH1F *h15 = (TH1F*)gPad->GetPrimitive("htemp");
	h15->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "3.00" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(16);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0350");
	TH1F *h16 = (TH1F*)gPad->GetPrimitive("htemp");
	h16->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "3.50" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(17);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0400");
	TH1F *h17 = (TH1F*)gPad->GetPrimitive("htemp");
	h17->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "4.00" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(18);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0500");
	TH1F *h18 = (TH1F*)gPad->GetPrimitive("htemp");
	h18->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "5.00" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(19);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0600");
	TH1F *h19 = (TH1F*)gPad->GetPrimitive("htemp");
	h19->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "6.00" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(20);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0700");
	TH1F *h20 = (TH1F*)gPad->GetPrimitive("htemp");
	h20->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "7.00" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(21);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0800");
	TH1F *h21 = (TH1F*)gPad->GetPrimitive("htemp");
	h21->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "8.00" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(22);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0900");
	TH1F *h22 = (TH1F*)gPad->GetPrimitive("htemp");
	h22->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "9.00" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;

	c1->cd(23);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_1000");
	TH1F *h23 = (TH1F*)gPad->GetPrimitive("htemp");
	h23->GetQuantiles(7,quant,quantPosition);
	cout << scientific << "10.0" << "\t" << quant[0] << "\t" << quant[1] << "\t" << quant[2] << "\t" << quant[3] << "\t" << quant[4] << "\t" << quant[5] << "\t" << quant[6] << endl;




}



























































































