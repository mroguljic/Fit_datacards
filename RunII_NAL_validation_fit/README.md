datacard.txt runs the fit in the NAL hadronic regions and semileptonic control regions simultaneously. Running the fit with
```combine -M FitDiagnostics -d datacard.txt --setParameters r=1 --saveWorkspace --saveShapes --saveWithUncertainties  --saveNormalizations   --cminDefaultMinimizerStrategy 0  --rMin 0 --rMax 10 -v 2 |& tee combine_output.txt```
Combine output and the fitDiagnostics.root are stored as well.
