
#include "TCanvas.h"
#include "TTree.h"
#include "TH1D.h"
#include "TRandom.h"
#include <iomanip>

using namespace std;


void plot_one_RR_Dis(){

	TString fileString = "./34Ar+a/calcRate/34Ar4He_1.root";
	Double_t quant[7];
    Double_t quantPosition[7] = {0.01,0.025,0.16,0.5,0.84,0.975,1.0};

	TFile *rootFile = new TFile(fileString);
	TTree *TEMPS = (TTree*)rootFile->Get("temps");

	TCanvas *c1 = new TCanvas("c1","Title is gonna Title");
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0100");
	TH1F *h1 = (TH1F*)gPad->GetPrimitive("htemp");
	h1->SetTitle("  ");
	h1->GetQuantiles(7,quant,quantPosition);
	h1->GetXaxis()->SetTitle("Reaction Rate @ T = 1.0 GK");
	h1->GetXaxis()->CenterTitle();
	h1->SetLineColor(kBlack);

	TEMPS->Draw("temp_0100>>hist1_A",TString::Format("temp_0100 >= %e && temp_0100<=%e",quant[1],quant[5]),"SAME");
	TH1F *hist1_95 = (TH1F*)gPad->GetPrimitive("hist1_A");
	hist1_95->SetFillColorAlpha(kOrange+1,0.35);
	hist1_95->SetLineColor(kBlack);


	TEMPS->Draw("temp_0100>>hist1_B",TString::Format("temp_0100 >= %e && temp_0100<=%e",quant[2],quant[4]),"SAME");
	TH1F *hist1_68 = (TH1F*)gPad->GetPrimitive("hist1_B");
	hist1_68->SetFillColorAlpha(kOrange+8,0.35);
	hist1_68->SetLineColor(kBlack);

	//TEMPS->Draw("temp_0030>>hist1_C",TString::Format("temp_0030 >= %e && temp_0030<=%e",quant[3]-.02*quant[3],quant[3]+.02*quant[3]),"SAME");
	//TH1F *hist1_med = (TH1F*)gPad->GetPrimitive("hist1_C");
	//hist1_med->SetFillColorAlpha(kRed+1,0.35);
	//hist1_med->SetLineColor(kBlack);


}

void plot_select_RR_Dis(){


	TString fileString = "./34Ar+a/calcRate/test.root";
	Double_t quant[7];
    Double_t quantPosition[7] = {0.01,0.025,0.16,0.5,0.84,0.975,1.0};

	TFile *rootFile = new TFile(fileString);
	TTree *TEMPS = (TTree*)rootFile->Get("temps");

	TCanvas *c1 = new TCanvas("c1","Title is gonna Title");
	c1->Divide(3,4);


	c1->cd(1);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0030");
	TH1F *h1 = (TH1F*)gPad->GetPrimitive("htemp");
	h1->SetTitle("T = 0.3 GK");
	h1->GetQuantiles(7,quant,quantPosition);

	TEMPS->Draw("temp_0030>>hist1_A",TString::Format("temp_0030 >= %e && temp_0030<=%e",quant[1],quant[5]),"SAME");
	TH1F *hist1_95 = (TH1F*)gPad->GetPrimitive("hist1_A");
	hist1_95->SetFillColorAlpha(30,0.35);


	TEMPS->Draw("temp_0030>>hist1_B",TString::Format("temp_0030 >= %e && temp_0030<=%e",quant[2],quant[4]),"SAME");
	TH1F *hist1_68 = (TH1F*)gPad->GetPrimitive("hist1_B");
	hist1_68->SetFillColorAlpha(32,0.35);

	c1->cd(2);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0040");
	TH1F *h2 = (TH1F*)gPad->GetPrimitive("htemp");
	h2->SetTitle("T = 0.4 GK");
	h2->GetQuantiles(7,quant,quantPosition);

	TEMPS->Draw("temp_0040>>hist2_A",TString::Format("temp_0040 >= %e && temp_0040<=%e",quant[1],quant[5]),"SAME");
	TH1F *hist2_95 = (TH1F*)gPad->GetPrimitive("hist2_A");
	hist2_95->SetFillColorAlpha(30,0.35);


	TEMPS->Draw("temp_0040>>hist2_B",TString::Format("temp_0040 >= %e && temp_0040<=%e",quant[2],quant[4]),"SAME");
	TH1F *hist2_68 = (TH1F*)gPad->GetPrimitive("hist2_B");
	hist2_68->SetFillColorAlpha(32,0.35);

	c1->cd(3);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0050");
	TH1F *h3 = (TH1F*)gPad->GetPrimitive("htemp");
	h3->SetTitle("T = 0.5 GK");
	h3->GetQuantiles(7,quant,quantPosition);

	TEMPS->Draw("temp_0050>>hist3_A",TString::Format("temp_0050 >= %e && temp_0050<=%e",quant[1],quant[5]),"SAME");
	TH1F *hist3_95 = (TH1F*)gPad->GetPrimitive("hist3_A");
	hist3_95->SetFillColorAlpha(30,0.35);


	TEMPS->Draw("temp_0050>>hist3_B",TString::Format("temp_0050 >= %e && temp_0050<=%e",quant[2],quant[4]),"SAME");
	TH1F *hist3_68 = (TH1F*)gPad->GetPrimitive("hist3_B");
	hist3_68->SetFillColorAlpha(32,0.35);

	c1->cd(4);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0060");
	TH1F *h4 = (TH1F*)gPad->GetPrimitive("htemp");
	h4->SetTitle("T = 0.6 GK");
	h4->GetQuantiles(7,quant,quantPosition);

	TEMPS->Draw("temp_0060>>hist4_A",TString::Format("temp_0060 >= %e && temp_0060<=%e",quant[1],quant[5]),"SAME");
	TH1F *hist4_95 = (TH1F*)gPad->GetPrimitive("hist4_A");
	hist4_95->SetFillColorAlpha(30,0.35);


	TEMPS->Draw("temp_0060>>hist4_B",TString::Format("temp_0060 >= %e && temp_0060<=%e",quant[2],quant[4]),"SAME");
	TH1F *hist4_68 = (TH1F*)gPad->GetPrimitive("hist4_B");
	hist4_68->SetFillColorAlpha(32,0.35);

	c1->cd(5);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0070");
	TH1F *h5 = (TH1F*)gPad->GetPrimitive("htemp");
	h5->SetTitle("T = 0.7 GK");
	h5->GetQuantiles(7,quant,quantPosition);

	TEMPS->Draw("temp_0070>>hist5_A",TString::Format("temp_0070 >= %e && temp_0070<=%e",quant[1],quant[5]),"SAME");
	TH1F *hist5_95 = (TH1F*)gPad->GetPrimitive("hist5_A");
	hist5_95->SetFillColorAlpha(30,0.35);


	TEMPS->Draw("temp_0070>>hist5_B",TString::Format("temp_0070 >= %e && temp_0070<=%e",quant[2],quant[4]),"SAME");
	TH1F *hist5_68 = (TH1F*)gPad->GetPrimitive("hist5_B");
	hist5_68->SetFillColorAlpha(32,0.35);

	c1->cd(6);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0080");
	TH1F *h6 = (TH1F*)gPad->GetPrimitive("htemp");
	h6->SetTitle("T = 0.8 GK");
	h6->GetQuantiles(7,quant,quantPosition);

	TEMPS->Draw("temp_0080>>hist6_A",TString::Format("temp_0080 >= %e && temp_0080<=%e",quant[1],quant[5]),"SAME");
	TH1F *hist6_95 = (TH1F*)gPad->GetPrimitive("hist6_A");
	hist6_95->SetFillColorAlpha(30,0.35);


	TEMPS->Draw("temp_0080>>hist6_B",TString::Format("temp_0080 >= %e && temp_0080<=%e",quant[2],quant[4]),"SAME");
	TH1F *hist6_68 = (TH1F*)gPad->GetPrimitive("hist6_B");
	hist6_68->SetFillColorAlpha(32,0.35);

	c1->cd(7);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0090");
	TH1F *h7 = (TH1F*)gPad->GetPrimitive("htemp");
	h7->SetTitle("T = 0.9 GK");
	h7->GetQuantiles(7,quant,quantPosition);

	TEMPS->Draw("temp_0090>>hist7_A",TString::Format("temp_0090 >= %e && temp_0090<=%e",quant[1],quant[5]),"SAME");
	TH1F *hist7_95 = (TH1F*)gPad->GetPrimitive("hist7_A");
	hist7_95->SetFillColorAlpha(30,0.35);


	TEMPS->Draw("temp_0090>>hist7_B",TString::Format("temp_0090 >= %e && temp_0090<=%e",quant[2],quant[4]),"SAME");
	TH1F *hist7_68 = (TH1F*)gPad->GetPrimitive("hist7_B");
	hist7_68->SetFillColorAlpha(32,0.35);

	c1->cd(8);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0100");
	TH1F *h8 = (TH1F*)gPad->GetPrimitive("htemp");
	h8->SetTitle("T = 1.0 GK");
	h8->GetQuantiles(7,quant,quantPosition);

	TEMPS->Draw("temp_0100>>hist8_A",TString::Format("temp_0100 >= %e && temp_0100<=%e",quant[1],quant[5]),"SAME");
	TH1F *hist8_95 = (TH1F*)gPad->GetPrimitive("hist8_A");
	hist8_95->SetFillColorAlpha(30,0.35);


	TEMPS->Draw("temp_0100>>hist8_B",TString::Format("temp_0100 >= %e && temp_0100<=%e",quant[2],quant[4]),"SAME");
	TH1F *hist8_68 = (TH1F*)gPad->GetPrimitive("hist8_B");
	hist8_68->SetFillColorAlpha(32,0.35);

	c1->cd(9);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0150");
	TH1F *h9 = (TH1F*)gPad->GetPrimitive("htemp");
	h9->SetTitle("T = 1,5 GK");
	h9->GetQuantiles(7,quant,quantPosition);

	TEMPS->Draw("temp_0150>>hist9_A",TString::Format("temp_0150 >= %e && temp_0150<=%e",quant[1],quant[5]),"SAME");
	TH1F *hist9_95 = (TH1F*)gPad->GetPrimitive("hist9_A");
	hist9_95->SetFillColorAlpha(30,0.35);


	TEMPS->Draw("temp_0150>>hist9_B",TString::Format("temp_0150 >= %e && temp_0150<=%e",quant[2],quant[4]),"SAME");
	TH1F *hist9_68 = (TH1F*)gPad->GetPrimitive("hist9_B");
	hist9_68->SetFillColorAlpha(32,0.35);

	c1->cd(10);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0200");
	TH1F *h10 = (TH1F*)gPad->GetPrimitive("htemp");
	h10->SetTitle("T = 2.0 GK");
	h10->GetQuantiles(7,quant,quantPosition);


	TEMPS->Draw("temp_0200>>hist10_A",TString::Format("temp_0200 >= %e && temp_0200<=%e",quant[1],quant[5]),"SAME");
	TH1F *hist10_95 = (TH1F*)gPad->GetPrimitive("hist10_A");
	hist10_95->SetFillColorAlpha(30,0.35);


	TEMPS->Draw("temp_0200>>hist10_B",TString::Format("temp_0200 >= %e && temp_0200<=%e",quant[2],quant[4]),"SAME");
	TH1F *hist10_68 = (TH1F*)gPad->GetPrimitive("hist10_B");
	hist10_68->SetFillColorAlpha(32,0.35);

	c1->cd(11);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0250");
	TH1F *h11 = (TH1F*)gPad->GetPrimitive("htemp");
	h11->SetTitle("T = 2.5 GK");
	h11->GetQuantiles(7,quant,quantPosition);


	TEMPS->Draw("temp_0250>>hist11_A",TString::Format("temp_0250 >= %e && temp_0250<=%e",quant[1],quant[5]),"SAME");
	TH1F *hist11_95 = (TH1F*)gPad->GetPrimitive("hist11_A");
	hist11_95->SetFillColorAlpha(30,0.35);


	TEMPS->Draw("temp_0250>>hist11_B",TString::Format("temp_0250 >= %e && temp_0250<=%e",quant[2],quant[4]),"SAME");
	TH1F *hist11_68 = (TH1F*)gPad->GetPrimitive("hist11_B");
	hist11_68->SetFillColorAlpha(32,0.35);

	c1->cd(12);
	gStyle->SetOptStat(0);
	TEMPS->Draw("temp_0300");
	TH1F *h12 = (TH1F*)gPad->GetPrimitive("htemp");
	h12->SetTitle("T = 3.0 GK");
	h12->GetQuantiles(7,quant,quantPosition);


	TEMPS->Draw("temp_0300>>hist12_A",TString::Format("temp_0300 >= %e && temp_0300<=%e",quant[1],quant[5]),"SAME");
	TH1F *hist12_95 = (TH1F*)gPad->GetPrimitive("hist12_A");
	hist12_95->SetFillColorAlpha(30,0.35);


	TEMPS->Draw("temp_0300>>hist12_B",TString::Format("temp_0300 >= %e && temp_0300<=%e",quant[2],quant[4]),"SAME");
	TH1F *hist12_68 = (TH1F*)gPad->GetPrimitive("hist12_B");
	hist12_68->SetFillColorAlpha(32,0.35);


}



























































































