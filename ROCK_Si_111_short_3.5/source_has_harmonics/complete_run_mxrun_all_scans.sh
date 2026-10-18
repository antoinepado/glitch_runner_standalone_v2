#!/bin/bash
set -e

mxrun --mpi=6 soleil_rock.instr angle_m2a_m2b=0.0046 reflec_material_M2A_M2B="B4C.dat" ie_value=0.45 position_cabane=32.7 Etohit=6950,8150 mosaic_value=0.5 delta_d_d_value=1e-8 hslitchamber=10e-3 vslitchamber=0.6e-3 -n1e7 -N1201
mxrun --mpi=6 soleil_rock.instr angle_m2a_m2b=0.006 reflec_material_M2A_M2B="B4C.dat" ie_value=0.5 position_cabane=32.7 Etohit=8030,9970 mosaic_value=0.5 delta_d_d_value=1e-8 -n1e7 -N1941
mxrun --mpi=6 soleil_rock_spare.instr angle_m2a_m2b=0.007 reflec_material_M2A_M2B="B4C.dat" ie_value=0.5 position_cabane=27 Etohit=4850,5656 mosaic_value=0.5 delta_d_d_value=1e-8 -n1e7 -N807
mxrun --mpi=6 soleil_rock.instr angle_m2a_m2b=0.0056 reflec_material_M2A_M2B="B4C.dat" ie_value=0.45 position_cabane=32.7 Etohit=6900,8250 mosaic_value=0.5 delta_d_d_value=1e-8 -n1e7 -N1351
mxrun --mpi=6 soleil_rock.instr angle_m2a_m2b=0.0055 reflec_material_M2A_M2B="B4C.dat" ie_value=0.5 position_cabane=32.7 Etohit=8780,9980 mosaic_value=0.5 delta_d_d_value=1e-8 reflec_material_filter="Al.txt" filter_thickness=200e-6 -n1e7 -N1201
mxrun --mpi=6 soleil_rock.instr angle_m2a_m2b=0.004 reflec_material_M2A_M2B="B4C.dat" ie_value=0.5 position_cabane=32.7 Etohit=6950,8100 mosaic_value=0.5 delta_d_d_value=1e-8 -n1e7 -N1151
mxrun --mpi=6 soleil_rock.instr angle_m2a_m2b=0.0056 reflec_material_M2A_M2B="B4C.dat" ie_value=0.5 position_cabane=32.7 Etohit=8100,9580 mosaic_value=0.5 delta_d_d_value=1e-8 hslitchamber=10e-3 vslitchamber=0.6e-3 -n1e7 -N1481
mxrun --mpi=6 soleil_rock.instr angle_m2a_m2b=0.0056 reflec_material_M2A_M2B="B4C.dat" ie_value=0.5 position_cabane=32 Etohit=7500,9600 mosaic_value=0.5 delta_d_d_value=1e-8 -n1e7 -N2101
mxrun --mpi=6 soleil_rock_spare.instr angle_m2a_m2b=0.0056 reflec_material_M2A_M2B="B4C.dat" ie_value=0.45 position_cabane=30 Etohit=7000,8950 mosaic_value=0.5 delta_d_d_value=1e-8 hslitchamber=1e-3 vslitchamber=0.5e-3 -n1e7 -N1951
