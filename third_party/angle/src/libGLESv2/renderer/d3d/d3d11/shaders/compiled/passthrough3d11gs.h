#if 0
//
// Generated by Microsoft (R) HLSL Shader Compiler 9.30.9200.16384
//
//
///
//
// Input signature:
//
// Name                 Index   Mask Register SysValue  Format   Used
// -------------------- ----- ------ -------- -------- ------- ------
// SV_POSITION              0   xyzw        0      POS   float   xyzw
// LAYER                    0   x           1     NONE    uint   x   
// TEXCOORD                 0   xyz         2     NONE   float   xyz 
//
//
// Output signature:
//
// Name                 Index   Mask Register SysValue  Format   Used
// -------------------- ----- ------ -------- -------- ------- ------
// SV_POSITION              0   xyzw        0      POS   float   xyzw
// SV_RENDERTARGETARRAYINDEX     0   x           1  RTINDEX    uint   x   
// TEXCOORD                 0   xyz         2     NONE   float   xyz 
//
gs_4_0
dcl_input_siv v[3][0].xyzw, position
dcl_input v[3][1].x
dcl_input v[3][2].xyz
dcl_temps 1
dcl_inputprimitive triangle 
dcl_outputtopology trianglestrip 
dcl_output_siv o0.xyzw, position
dcl_output_siv o1.x, rendertarget_array_index
dcl_output o2.xyz
dcl_maxout 3
mov r0.x, l(0)
loop 
  ige r0.y, r0.x, l(3)
  breakc_nz r0.y
  mov o0.xyzw, v[r0.x + 0][0].xyzw
  mov o1.x, v[r0.x + 0][1].x
  mov o2.xyz, v[r0.x + 0][2].xyzx
  emit 
  iadd r0.x, r0.x, l(1)
endloop 
ret 
// Approximately 11 instruction slots used
#endif

const BYTE g_GS_Passthrough3D[] =
{
     68,  88,  66,  67,  21,  92, 
    188, 203,  22,  49, 177, 239, 
    121, 233, 148, 135, 212,  27, 
    172, 209,   1,   0,   0,   0, 
     72,   3,   0,   0,   5,   0, 
      0,   0,  52,   0,   0,   0, 
    140,   0,   0,   0,   0,   1, 
      0,   0, 136,   1,   0,   0, 
    204,   2,   0,   0,  82,  68, 
     69,  70,  80,   0,   0,   0, 
      0,   0,   0,   0,   0,   0, 
      0,   0,   0,   0,   0,   0, 
     28,   0,   0,   0,   0,   4, 
     83,  71,   0,   1,   0,   0, 
     28,   0,   0,   0,  77, 105, 
     99, 114, 111, 115, 111, 102, 
    116,  32,  40,  82,  41,  32, 
     72,  76,  83,  76,  32,  83, 
    104,  97, 100, 101, 114,  32, 
     67, 111, 109, 112, 105, 108, 
    101, 114,  32,  57,  46,  51, 
     48,  46,  57,  50,  48,  48, 
     46,  49,  54,  51,  56,  52, 
      0, 171,  73,  83,  71,  78, 
    108,   0,   0,   0,   3,   0, 
      0,   0,   8,   0,   0,   0, 
     80,   0,   0,   0,   0,   0, 
      0,   0,   1,   0,   0,   0, 
      3,   0,   0,   0,   0,   0, 
      0,   0,  15,  15,   0,   0, 
     92,   0,   0,   0,   0,   0, 
      0,   0,   0,   0,   0,   0, 
      1,   0,   0,   0,   1,   0, 
      0,   0,   1,   1,   0,   0, 
     98,   0,   0,   0,   0,   0, 
      0,   0,   0,   0,   0,   0, 
      3,   0,   0,   0,   2,   0, 
      0,   0,   7,   7,   0,   0, 
     83,  86,  95,  80,  79,  83, 
     73,  84,  73,  79,  78,   0, 
     76,  65,  89,  69,  82,   0, 
     84,  69,  88,  67,  79,  79, 
     82,  68,   0, 171,  79,  83, 
     71,  78, 128,   0,   0,   0, 
      3,   0,   0,   0,   8,   0, 
      0,   0,  80,   0,   0,   0, 
      0,   0,   0,   0,   1,   0, 
      0,   0,   3,   0,   0,   0, 
      0,   0,   0,   0,  15,   0, 
      0,   0,  92,   0,   0,   0, 
      0,   0,   0,   0,   4,   0, 
      0,   0,   1,   0,   0,   0, 
      1,   0,   0,   0,   1,  14, 
      0,   0, 118,   0,   0,   0, 
      0,   0,   0,   0,   0,   0, 
      0,   0,   3,   0,   0,   0, 
      2,   0,   0,   0,   7,   8, 
      0,   0,  83,  86,  95,  80, 
     79,  83,  73,  84,  73,  79, 
     78,   0,  83,  86,  95,  82, 
     69,  78,  68,  69,  82,  84, 
     65,  82,  71,  69,  84,  65, 
     82,  82,  65,  89,  73,  78, 
     68,  69,  88,   0,  84,  69, 
     88,  67,  79,  79,  82,  68, 
      0, 171,  83,  72,  68,  82, 
     60,   1,   0,   0,  64,   0, 
      2,   0,  79,   0,   0,   0, 
     97,   0,   0,   5, 242,  16, 
     32,   0,   3,   0,   0,   0, 
      0,   0,   0,   0,   1,   0, 
      0,   0,  95,   0,   0,   4, 
     18,  16,  32,   0,   3,   0, 
      0,   0,   1,   0,   0,   0, 
     95,   0,   0,   4, 114,  16, 
     32,   0,   3,   0,   0,   0, 
      2,   0,   0,   0, 104,   0, 
      0,   2,   1,   0,   0,   0, 
     93,  24,   0,   1,  92,  40, 
      0,   1, 103,   0,   0,   4, 
    242,  32,  16,   0,   0,   0, 
      0,   0,   1,   0,   0,   0, 
    103,   0,   0,   4,  18,  32, 
     16,   0,   1,   0,   0,   0, 
      4,   0,   0,   0, 101,   0, 
      0,   3, 114,  32,  16,   0, 
      2,   0,   0,   0,  94,   0, 
      0,   2,   3,   0,   0,   0, 
     54,   0,   0,   5,  18,   0, 
     16,   0,   0,   0,   0,   0, 
      1,  64,   0,   0,   0,   0, 
      0,   0,  48,   0,   0,   1, 
     33,   0,   0,   7,  34,   0, 
     16,   0,   0,   0,   0,   0, 
     10,   0,  16,   0,   0,   0, 
      0,   0,   1,  64,   0,   0, 
      3,   0,   0,   0,   3,   0, 
      4,   3,  26,   0,  16,   0, 
      0,   0,   0,   0,  54,   0, 
      0,   7, 242,  32,  16,   0, 
      0,   0,   0,   0,  70,  30, 
    160,   0,  10,   0,  16,   0, 
      0,   0,   0,   0,   0,   0, 
      0,   0,  54,   0,   0,   7, 
     18,  32,  16,   0,   1,   0, 
      0,   0,  10,  16, 160,   0, 
     10,   0,  16,   0,   0,   0, 
      0,   0,   1,   0,   0,   0, 
     54,   0,   0,   7, 114,  32, 
     16,   0,   2,   0,   0,   0, 
     70,  18, 160,   0,  10,   0, 
     16,   0,   0,   0,   0,   0, 
      2,   0,   0,   0,  19,   0, 
      0,   1,  30,   0,   0,   7, 
     18,   0,  16,   0,   0,   0, 
      0,   0,  10,   0,  16,   0, 
      0,   0,   0,   0,   1,  64, 
      0,   0,   1,   0,   0,   0, 
     22,   0,   0,   1,  62,   0, 
      0,   1,  83,  84,  65,  84, 
    116,   0,   0,   0,  11,   0, 
      0,   0,   1,   0,   0,   0, 
      0,   0,   0,   0,   6,   0, 
      0,   0,   0,   0,   0,   0, 
      2,   0,   0,   0,   0,   0, 
      0,   0,   1,   0,   0,   0, 
      1,   0,   0,   0,   0,   0, 
      0,   0,   0,   0,   0,   0, 
      0,   0,   0,   0,   0,   0, 
      0,   0,   1,   0,   0,   0, 
      0,   0,   0,   0,   0,   0, 
      0,   0,   0,   0,   0,   0, 
      0,   0,   0,   0,   0,   0, 
      0,   0,  12,   0,   0,   0, 
      0,   0,   0,   0,   0,   0, 
      0,   0,   0,   0,   0,   0, 
      3,   0,   0,   0,   5,   0, 
      0,   0,   3,   0,   0,   0, 
      0,   0,   0,   0,   0,   0, 
      0,   0,   0,   0,   0,   0
};
