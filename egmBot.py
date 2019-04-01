import discord
import asyncio
import random
import os

client = discord.Client()


Single_size8 = ['1_1', '1_2', '1_3', '1_4', '2_1', '2_2', 'final']
Single_size16 = ['1_1', '1_2', '1_3', '1_4', '1_5', '1_6', '1_7', '1_8',
                 '2_1', '2_2', '2_3', '2_4',
                 '3_1', '3_2',
                 'final']
Single_size32 = ['1_1', '1_2', '1_3', '1_4', '1_5', '1_6', '1_7', '1_8',
                 '1_9', '1_10', '1_11', '1_12', '1_13', '1_14', '1_15', '1_16',
                 '2_1', '2_2', '2_3', '2_4', '2_5', '2_6', '2_7', '2_8',
                 '3_1', '3_2', '3_3', '3_4',
                 '4_1', '4_2',
                 'final']
Single_size64 = ['1_1', '1_2', '1_3', '1_4', '1_5', '1_6', '1_7', '1_8',
                 '1_9', '1_10', '1_11', '1_12', '1_13', '1_14', '1_15', '1_16',
                 '1_17', '1_18', '1_19', '1_20', '1_21', '1_22', '1_23', '1_24',
                 '1_25', '1_26', '1_27', '1_28', '1_29', '1_30', '1_31', '1_32',
                 '2_1', '2_2', '2_3', '2_4', '2_5', '2_6', '2_7', '2_8',
                 '2_9', '2_10', '2_11', '2_12', '2_13', '2_14', '2_15', '2_16',
                 '3_1', '3_2', '3_3', '3_4', '3_5', '3_6', '3_7', '3_8',
                 '4_1', '4_2', '4_3', '4_4',
                 '5_1', '5_2',
                 'final']

Single_size128 = ['1_1', '1_2', '1_3', '1_4', '1_5', '1_6', '1_7', '1_8',
                  '1_9', '1_10', '1_11', '1_12', '1_13', '1_14', '1_15', '1_16',
                  '1_17', '1_18', '1_19', '1_20', '1_21', '1_22', '1_23', '1_24',
                  '1_25', '1_26', '1_27', '1_28', '1_29', '1_30', '1_31', '1_32',
                  '1_33', '1_34', '1_35', '1_36', '1_37', '1_38', '1_39', '1_40',
                  '1_41', '1_42', '1_43', '1_44', '1_45', '1_46', '1_47', '1_48',
                  '1_49', '1_50', '1_51', '1_52', '1_53', '1_54', '1_55', '1_56',
                  '1_57', '1_58', '1_59', '1_60', '1_61', '1_62', '1_63', '1_64',
                  '2_1', '2_2', '2_3', '2_4', '2_5', '2_6', '2_7', '2_8',
                  '2_9', '2_10', '2_11', '2_12', '2_13', '2_14', '2_15', '2_16',
                  '2_17', '2_18', '2_19', '2_20', '2_21', '2_22', '2_23', '2_24',
                  '2_25', '2_26', '2_27', '2_28', '2_29', '2_30', '2_31', '2_32',
                  '3_1', '3_2', '3_3', '3_4', '3_5', '3_6', '3_7', '3_8',
                  '3_9', '3_10', '3_11', '3_12', '3_13', '3_14', '3_15', '3_16',
                  '4_1', '4_2', '4_3', '4_4', '4_5', '4_6', '4_7', '4_8',
                  '5_1', '5_2', '5_3', '5_4',
                  '6_1', '6_2',
                  'final']
Single_size256 = ['1_1', '1_2', '1_3', '1_4', '1_5', '1_6', '1_7', '1_8',
                  '1_9', '1_10', '1_11', '1_12', '1_13', '1_14', '1_15', '1_16',
                  '1_17', '1_18', '1_19', '1_20', '1_21', '1_22', '1_23', '1_24',
                  '1_25', '1_26', '1_27', '1_28', '1_29', '1_30', '1_31', '1_32',
                  '1_33', '1_34', '1_35', '1_36', '1_37', '1_38', '1_39', '1_40',
                  '1_41', '1_42', '1_43', '1_44', '1_45', '1_46', '1_47', '1_48',
                  '1_49', '1_50', '1_51', '1_52', '1_53', '1_54', '1_55', '1_56',
                  '1_57', '1_58', '1_59', '1_60', '1_61', '1_62', '1_63', '1_64',
                  '1_65', '1_66', '1_67', '1_68', '1_69', '1_70', '1_71', '1_72',
                  '1_73', '1_74', '1_75', '1_76', '1_77', '1_78', '1_79', '1_80',
                  '1_81', '1_82', '1_83', '1_84', '1_85', '1_86', '1_87', '1_88',
                  '1_89', '1_90', '1_91', '1_92', '1_93', '1_94', '1_95', '1_96',
                  '1_97', '1_98', '1_99', '1_100', '1_101', '1_102', '1_103', '1_104',
                  '1_105', '1_106', '1_107', '1_108', '1_109', '1_110', '1_111', '1_112',
                  '1_113', '1_114', '1_115', '1_116', '1_117', '1_118', '1_119', '1_120',
                  '1_121', '1_122', '1_123', '1_124', '1_125', '1_126', '1_127', '1_128',
                  '2_1', '2_2', '2_3', '2_4', '2_5', '2_6', '2_7', '2_8',
                  '2_9', '2_10', '2_11', '2_12', '2_13', '2_14', '2_15', '2_16',
                  '2_17', '2_18', '2_19', '2_20', '2_21', '2_22', '2_23', '2_24',
                  '2_25', '2_26', '2_27', '2_28', '2_29', '2_30', '2_31', '2_32',
                  '2_33', '2_34', '2_35', '2_36', '2_37', '2_38', '2_39', '2_40',
                  '2_41', '2_42', '2_43', '2_44', '2_45', '2_46', '2_47', '2_48',
                  '2_49', '2_50', '2_51', '2_52', '2_53', '2_54', '2_55', '2_56',
                  '2_57', '2_58', '2_59', '2_60', '2_61', '2_62', '2_63', '2_64',
                  '3_1', '3_2', '3_3', '3_4', '3_5', '3_6', '3_7', '3_8',
                  '3_9', '3_10', '3_11', '3_12', '3_13', '3_14', '3_15', '3_16',
                  '3_17', '3_18', '3_19', '3_20', '3_21', '3_22', '3_23', '3_24',
                  '3_25', '3_26', '3_27', '3_28', '3_29', '3_30', '3_31', '3_32',
                  '4_1', '4_2', '4_3', '4_4', '4_5', '4_6', '4_7', '4_8',
                  '4_9', '4_10', '4_11', '4_12', '4_13', '4_14', '4_15', '4_16',
                  '5_1', '5_2', '5_3', '5_4', '5_5', '5_6', '5_7', '5_8',
                  '6_1', '6_2', '6_3', '6_4',
                  '7_1', '7_2',
                  'final']
Double_size8 = ['winners_1_1', 'winners_1_2', 'winners_1_3', 'winners_1_4',
                'winners_2_1', 'winners_2_2',
                'winners_final',
                'losers_1_1', 'losers_1_2',
                'losers_2_1', 'losers_2_2',
                'losers_3_1',
                'losers_final',
                'Grand_final']
Double_size16 = ['winners_1_1', 'winners_1_2', 'winners_1_3', 'winners_1_4',
                 'winners_1_5', 'winners_1_6', 'winners_1_7', 'winners_1_8',
                 'winners_2_1', 'winners_2_2', 'winners_2_3', 'winners_2_4',
                 'winners_3_1', 'winners_3_2',
                 'winners_final',
                 'losers_1_1', 'losers_1_2', 'losers_1_3', 'losers_1_4',
                 'losers_2_1', 'losers_2_2', 'losers_2_3', 'losers_2_4',
                 'losers_3_1', 'losers_3_2',
                 'losers_4_1', 'losers_4_2',
                 'losers_5_1',
                 'losers_final',
                 'Grand_final']
Double_size32 = ['winners_1_1', 'winners_1_2', 'winners_1_3', 'winners_1_4',
                 'winners_1_5', 'winners_1_6', 'winners_1_7', 'winners_1_8',
                 'winners_1_9', 'winners_1_10', 'winners_1_11', 'winners_1_12',
                 'winners_1_13', 'winners_1_14', 'winners_1_15', 'winners_1_16',
                 'winners_2_1', 'winners_2_2', 'winners_2_3', 'winners_2_4',
                 'winners_2_5', 'winners_2_6', 'winners_2_7', 'winners_2_8',
                 'winners_3_1', 'winners_3_2', 'winners_3_3', 'winners_3_4',
                 'winners_4_1', 'winners_4_2',
                 'winners_final',
                 'losers_1_1', 'losers_1_2', 'losers_1_3', 'losers_1_4',
                 'losers_1_5', 'losers_1_6', 'losers_1_7', 'losers_1_8',
                 'losers_2_1', 'losers_2_2', 'losers_2_3', 'losers_2_4',
                 'losers_2_5', 'losers_2_6', 'losers_2_7', 'losers_2_8',
                 'losers_3_1', 'losers_3_2', 'losers_3_3', 'losers_3_4',
                 'losers_4_1', 'losers_4_2', 'losers_4_3', 'losers_4_4',
                 'losers_5_1', 'losers_5_2',
                 'losers_6_1', 'losers_6_2',
                 'losers_7_1',
                 'losers_final',
                 'Grand_final']

Double_size64 = ['winners_1_1', 'winners_1_2', 'winners_1_3', 'winners_1_4',
                 'winners_1_5', 'winners_1_6', 'winners_1_7', 'winners_1_8',
                 'winners_1_9', 'winners_1_10', 'winners_1_11', 'winners_1_12',
                 'winners_1_13', 'winners_1_14', 'winners_1_15', 'winners_1_16',
                 'winners_1_17', 'winners_1_18', 'winners_1_19', 'winners_1_20',
                 'winners_1_21', 'winners_1_22', 'winners_1_23', 'winners_1_24',
                 'winners_1_25', 'winners_1_26', 'winners_1_27', 'winners_1_28',
                 'winners_1_29', 'winners_1_30', 'winners_1_31', 'winners_1_32',
                 'winners_2_1', 'winners_2_2', 'winners_2_3', 'winners_2_4',
                 'winners_2_5', 'winners_2_6', 'winners_2_7', 'winners_2_8',
                 'winners_2_9', 'winners_2_10', 'winners_2_11', 'winners_2_12',
                 'winners_2_13', 'winners_2_14', 'winners_2_15', 'winners_2_16',
                 'winners_3_1', 'winners_3_2', 'winners_3_3', 'winners_3_4',
                 'winners_3_5', 'winners_3_6', 'winners_3_7', 'winners_3_8',
                 'winners_4_1', 'winners_4_2', 'winners_4_3', 'winners_4_4',
                 'winners_5_1', 'winners_5_2',
                 'winners_final',
                 'losers_1_1', 'losers_1_2', 'losers_1_3', 'losers_1_4',
                 'losers_1_5', 'losers_1_6', 'losers_1_7', 'losers_1_8',
                 'losers_1_9', 'losers_1_10', 'losers_1_11', 'losers_1_12',
                 'losers_1_13', 'losers_1_14', 'losers_1_15', 'losers_1_16',
                 'losers_2_1', 'losers_2_2', 'losers_2_3', 'losers_2_4',
                 'losers_2_5', 'losers_2_6', 'losers_2_7', 'losers_2_8',
                 'losers_2_9', 'losers_2_10', 'losers_2_11', 'losers_2_12',
                 'losers_2_13', 'losers_2_14', 'losers_2_15', 'losers_2_16',
                 'losers_3_1', 'losers_3_2', 'losers_3_3', 'losers_3_4',
                 'losers_3_5', 'losers_3_6', 'losers_3_7', 'losers_3_8',
                 'losers_4_1', 'losers_4_2', 'losers_4_3', 'losers_4_4',
                 'losers_4_5', 'losers_4_6', 'losers_4_7', 'losers_4_8',
                 'losers_5_1', 'losers_5_2', 'losers_5_3', 'losers_5_4',
                 'losers_6_1', 'losers_6_2', 'losers_6_3', 'losers_6_4',
                 'losers_7_1', 'losers_7_2',
                 'losers_8_1', 'losers_8_2',
                 'losers_9_1',
                 'losers_final',
                 'Grand_final']

Double_size128 = ['winners_1_1', 'winners_1_2', 'winners_1_3', 'winners_1_4',
                  'winners_1_5', 'winners_1_6', 'winners_1_7', 'winners_1_8',
                  'winners_1_9', 'winners_1_10', 'winners_1_11', 'winners_1_12',
                  'winners_1_13', 'winners_1_14', 'winners_1_15', 'winners_1_16',
                  'winners_1_17', 'winners_1_18', 'winners_1_19', 'winners_1_20',
                  'winners_1_21', 'winners_1_22', 'winners_1_23', 'winners_1_24',
                  'winners_1_25', 'winners_1_26', 'winners_1_27', 'winners_1_28',
                  'winners_1_29', 'winners_1_30', 'winners_1_31', 'winners_1_32',
                  'winners_1_33', 'winners_1_34', 'winners_1_35', 'winners_1_36',
                  'winners_1_37', 'winners_1_38', 'winners_1_39', 'winners_1_40',
                  'winners_1_41', 'winners_1_42', 'winners_1_43', 'winners_1_44',
                  'winners_1_45', 'winners_1_46', 'winners_1_47', 'winners_1_48',
                  'winners_1_49', 'winners_1_50', 'winners_1_51', 'winners_1_52',
                  'winners_1_53', 'winners_1_54', 'winners_1_55', 'winners_1_56',
                  'winners_1_57', 'winners_1_58', 'winners_1_59', 'winners_1_60',
                  'winners_1_61', 'winners_1_62', 'winners_1_63', 'winners_1_64',
                  'winners_2_1', 'winners_2_2', 'winners_2_3', 'winners_2_4',
                  'winners_2_5', 'winners_2_6', 'winners_2_7', 'winners_2_8',
                  'winners_2_9', 'winners_2_10', 'winners_2_11', 'winners_2_12',
                  'winners_2_13', 'winners_2_14', 'winners_2_15', 'winners_2_16',
                  'winners_2_17', 'winners_2_18', 'winners_2_19', 'winners_2_20',
                  'winners_2_21', 'winners_2_22', 'winners_2_23', 'winners_2_24',
                  'winners_2_25', 'winners_2_26', 'winners_2_27', 'winners_2_28',
                  'winners_2_29', 'winners_2_30', 'winners_2_31', 'winners_2_32',
                  'winners_3_1', 'winners_3_2', 'winners_3_3', 'winners_3_4',
                  'winners_3_5', 'winners_3_6', 'winners_3_7', 'winners_3_8',
                  'winners_3_9', 'winners_3_10', 'winners_3_11', 'winners_3_12',
                  'winners_3_13', 'winners_3_14', 'winners_3_15', 'winners_3_16',
                  'winners_4_1', 'winners_4_2', 'winners_4_3', 'winners_4_4',
                  'winners_4_5', 'winners_4_6', 'winners_4_7', 'winners_4_8',
                  'winners_5_1', 'winners_5_2', 'winners_5_3', 'winners_5_4',
                  'winners_6_1', 'winners_6_2',
                  'winners_final',
                  'losers_1_1', 'losers_1_2', 'losers_1_3', 'losers_1_4',
                  'losers_1_5', 'losers_1_6', 'losers_1_7', 'losers_1_8',
                  'losers_1_9', 'losers_1_10', 'losers_1_11', 'losers_1_12',
                  'losers_1_13', 'losers_1_14', 'losers_1_15', 'losers_1_16',
                  'losers_1_17', 'losers_1_18', 'losers_1_19', 'losers_1_20',
                  'losers_1_21', 'losers_1_22', 'losers_1_23', 'losers_1_24',
                  'losers_1_25', 'losers_1_26', 'losers_1_27', 'losers_1_28',
                  'losers_1_29', 'losers_1_30', 'losers_1_31', 'losers_1_32',
                  'losers_2_1', 'losers_2_2', 'losers_2_3', 'losers_2_4',
                  'losers_2_5', 'losers_2_6', 'losers_2_7', 'losers_2_8',
                  'losers_2_9', 'losers_2_10', 'losers_2_11', 'losers_2_12',
                  'losers_2_13', 'losers_2_14', 'losers_2_15', 'losers_2_16',
                  'losers_2_17', 'losers_2_18', 'losers_2_19', 'losers_2_20',
                  'losers_2_21', 'losers_2_22', 'losers_2_23', 'losers_2_24',
                  'losers_2_25', 'losers_2_26', 'losers_2_27', 'losers_2_28',
                  'losers_2_29', 'losers_2_30', 'losers_2_31', 'losers_2_32',
                  'losers_3_1', 'losers_3_2', 'losers_3_3', 'losers_3_4',
                  'losers_3_5', 'losers_3_6', 'losers_3_7', 'losers_3_8',
                  'losers_3_9', 'losers_3_10', 'losers_3_11', 'losers_3_12',
                  'losers_3_13', 'losers_3_14', 'losers_3_15', 'losers_3_16',
                  'losers_4_1', 'losers_4_2', 'losers_4_3', 'losers_4_4',
                  'losers_4_5', 'losers_4_6', 'losers_4_7', 'losers_4_8',
                  'losers_4_9', 'losers_4_10', 'losers_4_11', 'losers_4_12',
                  'losers_4_13', 'losers_4_14', 'losers_4_15', 'losers_4_16',
                  'losers_5_1', 'losers_5_2', 'losers_5_3', 'losers_5_4',
                  'losers_5_5', 'losers_5_6', 'losers_5_7', 'losers_5_8',
                  'losers_6_1', 'losers_6_2', 'losers_6_3', 'losers_6_4',
                  'losers_6_5', 'losers_6_6', 'losers_6_7', 'losers_6_8',
                  'losers_7_1', 'losers_7_2', 'losers_7_3', 'losers_7_4',
                  'losers_8_1', 'losers_8_2', 'losers_8_3', 'losers_8_4',
                  'losers_9_1', 'losers_9_2',
                  'losers_10_1', 'losers_10_2',
                  'losers_11_1',
                  'losers_final',
                  'Grand_final']

Double_size256 = ['winners_1_1', 'winners_1_2', 'winners_1_3', 'winners_1_4',
                  'winners_1_5', 'winners_1_6', 'winners_1_7', 'winners_1_8',
                  'winners_1_9', 'winners_1_10', 'winners_1_11', 'winners_1_12',
                  'winners_1_13', 'winners_1_14', 'winners_1_15', 'winners_1_16',
                  'winners_1_17', 'winners_1_18', 'winners_1_19', 'winners_1_20',
                  'winners_1_21', 'winners_1_22', 'winners_1_23', 'winners_1_24',
                  'winners_1_25', 'winners_1_26', 'winners_1_27', 'winners_1_28',
                  'winners_1_29', 'winners_1_30', 'winners_1_31', 'winners_1_32',
                  'winners_1_33', 'winners_1_34', 'winners_1_35', 'winners_1_36',
                  'winners_1_37', 'winners_1_38', 'winners_1_39', 'winners_1_40',
                  'winners_1_41', 'winners_1_42', 'winners_1_43', 'winners_1_44',
                  'winners_1_45', 'winners_1_46', 'winners_1_47', 'winners_1_48',
                  'winners_1_49', 'winners_1_50', 'winners_1_51', 'winners_1_52',
                  'winners_1_53', 'winners_1_54', 'winners_1_55', 'winners_1_56',
                  'winners_1_57', 'winners_1_58', 'winners_1_59', 'winners_1_60',
                  'winners_1_61', 'winners_1_62', 'winners_1_63', 'winners_1_64',
                  'winners_1_65', 'winners_1_66', 'winners_1_67', 'winners_1_68',
                  'winners_1_69', 'winners_1_70', 'winners_1_71', 'winners_1_72',
                  'winners_1_73', 'winners_1_74', 'winners_1_75', 'winners_1_76',
                  'winners_1_77', 'winners_1_78', 'winners_1_79', 'winners_1_80',
                  'winners_1_81', 'winners_1_82', 'winners_1_83', 'winners_1_84',
                  'winners_1_85', 'winners_1_86', 'winners_1_87', 'winners_1_88',
                  'winners_1_89', 'winners_1_90', 'winners_1_91', 'winners_1_92',
                  'winners_1_93', 'winners_1_94', 'winners_1_95', 'winners_1_96',
                  'winners_1_97', 'winners_1_98', 'winners_1_99', 'winners_1_100',
                  'winners_1_101', 'winners_1_102', 'winners_1_103', 'winners_1_104',
                  'winners_1_105', 'winners_1_106', 'winners_1_107', 'winners_1_108',
                  'winners_1_109', 'winners_1_110', 'winners_1_111', 'winners_1_112',
                  'winners_1_113', 'winners_1_114', 'winners_1_115', 'winners_1_116',
                  'winners_1_117', 'winners_1_118', 'winners_1_119', 'winners_1_120',
                  'winners_1_121', 'winners_1_122', 'winners_1_123', 'winners_1_124',
                  'winners_1_125', 'winners_1_126', 'winners_1_127', 'winners_1_128',
                  'winners_2_1', 'winners_2_2', 'winners_2_3', 'winners_2_4',
                  'winners_2_5', 'winners_2_6', 'winners_2_7', 'winners_2_8',
                  'winners_2_9', 'winners_2_10', 'winners_2_11', 'winners_2_12',
                  'winners_2_13', 'winners_2_14', 'winners_2_15', 'winners_2_16',
                  'winners_2_17', 'winners_2_18', 'winners_2_19', 'winners_2_20',
                  'winners_2_21', 'winners_2_22', 'winners_2_23', 'winners_2_24',
                  'winners_2_25', 'winners_2_26', 'winners_2_27', 'winners_2_28',
                  'winners_2_29', 'winners_2_30', 'winners_2_31', 'winners_2_32',
                  'winners_2_33', 'winners_2_34', 'winners_2_35', 'winners_2_36',
                  'winners_2_37', 'winners_2_38', 'winners_2_39', 'winners_2_40',
                  'winners_2_41', 'winners_2_42', 'winners_2_43', 'winners_2_44',
                  'winners_2_45', 'winners_2_46', 'winners_2_47', 'winners_2_48',
                  'winners_2_49', 'winners_2_50', 'winners_2_51', 'winners_2_52',
                  'winners_2_53', 'winners_2_54', 'winners_2_55', 'winners_2_56',
                  'winners_2_57', 'winners_2_58', 'winners_2_59', 'winners_2_60',
                  'winners_2_61', 'winners_2_62', 'winners_2_63', 'winners_2_64',
                  'winners_3_1', 'winners_3_2', 'winners_3_3', 'winners_3_4',
                  'winners_3_5', 'winners_3_6', 'winners_3_7', 'winners_3_8',
                  'winners_3_9', 'winners_3_10', 'winners_3_11', 'winners_3_12',
                  'winners_3_13', 'winners_3_14', 'winners_3_15', 'winners_3_16',
                  'winners_3_17', 'winners_3_18', 'winners_3_19', 'winners_3_20',
                  'winners_3_21', 'winners_3_22', 'winners_3_23', 'winners_3_24',
                  'winners_3_25', 'winners_3_26', 'winners_3_27', 'winners_3_28',
                  'winners_3_29', 'winners_3_30', 'winners_3_31', 'winners_3_32',
                  'winners_4_1', 'winners_4_2', 'winners_4_3', 'winners_4_4',
                  'winners_4_5', 'winners_4_6', 'winners_4_7', 'winners_4_8',
                  'winners_4_9', 'winners_4_10', 'winners_4_11', 'winners_4_12',
                  'winners_4_13', 'winners_4_14', 'winners_4_15', 'winners_4_16',
                  'winners_5_1', 'winners_5_2', 'winners_5_3', 'winners_5_4',
                  'winners_5_5', 'winners_5_6', 'winners_5_7', 'winners_5_8',
                  'winners_6_1', 'winners_6_2', 'winners_6_3', 'winners_6_4',
                  'winners_7_3', 'winners_7_4',
                  'winners_final',
                  'losers_1_1', 'losers_1_2', 'losers_1_3', 'losers_1_4',
                  'losers_1_5', 'losers_1_6', 'losers_1_7', 'losers_1_8',
                  'losers_1_9', 'losers_1_10', 'losers_1_11', 'losers_1_12',
                  'losers_1_13', 'losers_1_14', 'losers_1_15', 'losers_1_16',
                  'losers_1_17', 'losers_1_18', 'losers_1_19', 'losers_1_20',
                  'losers_1_21', 'losers_1_22', 'losers_1_23', 'losers_1_24',
                  'losers_1_25', 'losers_1_26', 'losers_1_27', 'losers_1_28',
                  'losers_1_29', 'losers_1_30', 'losers_1_31', 'losers_1_32',
                  'losers_1_33', 'losers_1_34', 'losers_1_35', 'losers_1_36',
                  'losers_1_37', 'losers_1_38', 'losers_1_39', 'losers_1_40',
                  'losers_1_41', 'losers_1_42', 'losers_1_43', 'losers_1_44',
                  'losers_1_45', 'losers_1_46', 'losers_1_47', 'losers_1_48',
                  'losers_1_49', 'losers_1_50', 'losers_1_51', 'losers_1_52',
                  'losers_1_53', 'losers_1_54', 'losers_1_55', 'losers_1_56',
                  'losers_1_57', 'losers_1_58', 'losers_1_59', 'losers_1_60',
                  'losers_1_61', 'losers_1_62', 'losers_1_63', 'losers_1_64',
                  'losers_2_1', 'losers_2_2', 'losers_2_3', 'losers_2_4',
                  'losers_2_5', 'losers_2_6', 'losers_2_7', 'losers_2_8',
                  'losers_2_9', 'losers_2_10', 'losers_2_11', 'losers_2_12',
                  'losers_2_13', 'losers_2_14', 'losers_2_15', 'losers_2_16',
                  'losers_2_17', 'losers_2_18', 'losers_2_19', 'losers_2_20',
                  'losers_2_21', 'losers_2_22', 'losers_2_23', 'losers_2_24',
                  'losers_2_25', 'losers_2_26', 'losers_2_27', 'losers_2_28',
                  'losers_2_29', 'losers_2_30', 'losers_2_31', 'losers_2_32',
                  'losers_2_33', 'losers_2_34', 'losers_2_35', 'losers_2_36',
                  'losers_2_37', 'losers_2_38', 'losers_2_39', 'losers_2_40',
                  'losers_2_41', 'losers_2_42', 'losers_2_43', 'losers_2_44',
                  'losers_2_45', 'losers_2_46', 'losers_2_47', 'losers_2_48',
                  'losers_2_49', 'losers_2_50', 'losers_2_51', 'losers_2_52',
                  'losers_2_53', 'losers_2_54', 'losers_2_55', 'losers_2_56',
                  'losers_2_57', 'losers_2_58', 'losers_2_59', 'losers_2_60',
                  'losers_2_61', 'losers_2_62', 'losers_2_63', 'losers_2_64',
                  'losers_3_1', 'losers_3_2', 'losers_3_3', 'losers_3_4',
                  'losers_3_5', 'losers_3_6', 'losers_3_7', 'losers_3_8',
                  'losers_3_9', 'losers_3_10', 'losers_3_11', 'losers_3_12',
                  'losers_3_13', 'losers_3_14', 'losers_3_15', 'losers_3_16',
                  'losers_3_17', 'losers_3_18', 'losers_3_19', 'losers_3_20',
                  'losers_3_21', 'losers_3_22', 'losers_3_23', 'losers_3_24',
                  'losers_3_25', 'losers_3_26', 'losers_3_27', 'losers_3_28',
                  'losers_3_29', 'losers_3_30', 'losers_3_31', 'losers_3_32',
                  'losers_4_1', 'losers_4_2', 'losers_4_3', 'losers_4_4',
                  'losers_4_5', 'losers_4_6', 'losers_4_7', 'losers_4_8',
                  'losers_4_9', 'losers_4_10', 'losers_4_11', 'losers_4_12',
                  'losers_4_13', 'losers_4_14', 'losers_4_15', 'losers_4_16',
                  'losers_4_17', 'losers_4_18', 'losers_4_19', 'losers_4_20',
                  'losers_4_21', 'losers_4_22', 'losers_4_23', 'losers_4_24',
                  'losers_4_25', 'losers_4_26', 'losers_4_27', 'losers_4_28',
                  'losers_4_29', 'losers_4_30', 'losers_4_31', 'losers_4_32',
                  'losers_5_1', 'losers_5_2', 'losers_5_3', 'losers_5_4',
                  'losers_5_5', 'losers_5_6', 'losers_5_7', 'losers_5_8',
                  'losers_5_9', 'losers_5_10', 'losers_5_11', 'losers_5_12',
                  'losers_5_13', 'losers_5_14', 'losers_5_15', 'losers_5_16',
                  'losers_6_1', 'losers_6_2', 'losers_6_3', 'losers_6_4',
                  'losers_6_5', 'losers_6_6', 'losers_6_7', 'losers_6_8',
                  'losers_6_9', 'losers_6_10', 'losers_6_11', 'losers_6_12',
                  'losers_6_13', 'losers_6_14', 'losers_6_15', 'losers_6_16',
                  'losers_7_1', 'losers_7_2', 'losers_7_3', 'losers_7_4',
                  'losers_7_5', 'losers_7_6', 'losers_7_7', 'losers_7_8',
                  'losers_8_1', 'losers_8_2', 'losers_8_3', 'losers_8_4',
                  'losers_8_5', 'losers_8_6', 'losers_8_7', 'losers_8_8',
                  'losers_9_1', 'losers_9_2', 'losers_9_3', 'losers_9_4',
                  'losers_10_1', 'losers_10_2', 'losers_10_3', 'losers_10_4',
                  'losers_11_1', 'losers_11_2',
                  'losers_12_1', 'losers_12_2',
                  'losers_13_1',
                  'losers_final',
                  'Grand_final']

CoD_esports_Rule = []
CoD_GA_Rule = []
CoD_CES_Rule =[]
HPMap =['Arsenal', 'Frequency', 'Gridlock', 'Hacienda', 'Seaside']
SDMap =['Arsenal', 'Frequency', 'Gridlock', 'Hacienda', 'Payload']
CTRMap =['Arsenal', 'Frequency', 'Gridlock', 'Seaside']


onoff = 0



cmd = '''
    プレイヤーが使えるコマンドは以下です。英数字と記号は半角で正確に入力してください。 ///以降はコマンドの説明です。

    !eスポーツルール   ///eスポーツのルールを一覧出来ます。

    !GA              ///EGM運営が把握しているGAです。GAに関しての扱いは各大会運営にお任せしております。強要はNGですよ〜

    !CES             ///CESルールを一覧できます

    !揃いました        ///運営が点呼チャットで点呼開始した後に送信してください。これを言わないとボットに催促されます

    !勝ちました        ///その試合の終了時(例えばBO5なら3マップ取得した時)に送信してください。必ず勝利側が送信してください。

    '''
@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')

    channel = ([channel.id for channel in client.get_all_channels()])
    print(channel)
    user = ([member.display_name for member in client.get_all_members()])
    print('userlist')
    print(user)
    print(discord.__version__)



'''
@client.event # イベントを受信するための構文（デコレータ）
async def on_message(message): # 発言を受信したら処理をする関数
    if message.content.startswith('!clean'):
        clean_flag = True
        while (clean_flag):
            msgs = [msg async for msg in client.logs_from(message.channel)]
            if len(msgs) > 1:
                await client.delete_messages(msgs)
            else:
                clean_flag = False
                await client.send_message(message.channel, 'ログの全削除が完了しました')
'''


@client.event
async def on_message(message):
    global onoff
    global cmd
    global l
    if message.channel.name == '設定':
        if message.content.startswith('!rim'):
            ch = [channel.id for channel in message.server.channels]
            for i in ch:
                channel = client.get_channel(i)
                await client.delete_channel(channel)
            await client.create_channel(message.server, '設定', type=discord.ChannelType.text)
            await client.create_channel(message.server, '点呼', type=discord.ChannelType.text)

    #if message.content.startswitch('!bot'):
        #await client.crate_channel(message.server, 'bot', type=discord.ChannelType.text)

    #シングル サイズ8
        if message.content.startswith('Single size 8'):
            for i in Single_size8:
                channel_name = i
                await client.create_channel(message.server, channel_name, type=discord.ChannelType.text)
            await client.send_message(message.channel,  'シングルイリミネーション チームサイズ8のチャンネルを作成しました')
            await client.send_message(message.channel, cmd)
    #シングル サイズ16
        if message.content.startswith('Single size 16'):
            for i in Single_size16:
                channel_name = i
                await client.create_channel(message.server, channel_name, type=discord.ChannelType.text)
            await client.send_message(message.channel,  'シングルイリミネーション チームサイズ16のチャンネルを作成しました')
    #シングル サイズ32
        if message.content.startswith('Single size 32'):
            for i in Single_size32:
                channel_name = i
                await client.create_channel(message.server, channel_name, type=discord.ChannelType.text)
            await client.send_message(message.channel,  'シングルイリミネーション チームサイズ32のチャンネルを作成しました')
    #シングル サイズ64
        if message.content.startswith('Single size 64'):
            for i in Single_size64:
                channel_name = i
                await client.create_channel(message.server, channel_name, type=discord.ChannelType.text)
            await client.send_message(message.channel,  'シングルイリミネーション チームサイズ64のチャンネルを作成しました')
    #シングル サイズ128
        if message.content.startswith('Single size 128'):
            for i in Single_size128:
                channel_name = i
                await client.create_channel(message.server, channel_name, type=discord.ChannelType.text)
            await client.send_message(message.channel,  'シングルイリミネーション チームサイズ128のチャンネルを作成しました')
    #シングル サイズ256
        if message.content.startswith('Single size 256'):
            for i in Single_size256:
                channel_name = i
                await client.create_channel(message.server, channel_name, type=discord.ChannelType.text)
            await client.send_message(message.channel,  'シングルイリミネーション チームサイズ256のチャンネルを作成しました')
    #ダブル サイズ8
        if message.content.startswith('Double size 8'):
            for i in Double_size8:
                channel_name = i
                await client.create_channel(message.server, channel_name, type=discord.ChannelType.text)
            await client.send_message(message.channel,  'ダブルイリミネーション チームサイズ8のチャンネルを作成しました')
    #ダブル サイズ16
        if message.content.startswith('Double size 16'):
            for i in Double_size16:
                channel_name = i
                await client.create_channel(message.server, channel_name, type=discord.ChannelType.text)
            await client.send_message(message.channel,  'ダブルイリミネーション チームサイズ16のチャンネルを作成しました')
    #ダブル サイズ32
        if message.content.startswith('Double size 32'):
            for i in Double_size32:
                channel_name = i
                await client.create_channel(message.server, channel_name, type=discord.ChannelType.text)
            await client.send_message(message.channel,  'ダブルイリミネーション チームサイズ32のチャンネルを作成しました')
    #ダブル サイズ64
        if message.content.startswith('Double size 64'):
            for i in Double_size64:
                channel_name = i
                await client.create_channel(message.server, channel_name, type=discord.ChannelType.text)
            await client.send_message(message.channel,  'ダブルイリミネーション チームサイズ64のチャンネルを作成しました')
    #ダブル サイズ128
        if message.content.startswith('Double size 128'):
            for i in Double_size128:
                channel_name = i
                await client.create_channel(message.server, channel_name, type=discord.ChannelType.text)
            await client.send_message(message.channel,  'ダブルイリミネーション チームサイズ128のチャンネルを作成しました')
    #ダブル サイズ256
        if message.content.startswith('Double size 256'):
            for i in Double_size256:
                channel_name = i
                await client.create_channel(message.server, channel_name, type=discord.ChannelType.text)
            await client.send_message(message.channel,  'ダブルイリミネーション チームサイズ256のチャンネルを作成しました')

    if message.content.startswith('!勝ちました') or message.content.startswith('!win') or message.content.startswith('!勝ち') or message.content.startswith('！勝ちました') or message.content.startswith('!WIN'):
        ch = [channel.id for channel in client.get_all_channels()]
        l = []
        for i in ch:
            channel = client.get_channel(i)
            l.append(channel.name)

        if message.channel.name == '1_1':
            msg = 'おめでとうございます。勝利チームは #2_1 のチャットで待機してください'
            await client.send_message(message.channel, msg)
        if message.channel.name == 'winners_1_1':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_1 のチャットで待機してください')
            await client.send_message(message.channel, '敗北チームは #losers_1_1 のチャットで待機してください')
        if message.channel.name == '1_2':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_1 のチャットで待機してください')
        if message.channel.name == 'winners_1_2':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_1 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_1 のチャットで待機してください')
        if message.channel.name == '1_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_2 のチャットで待機してください')
        if message.channel.name == 'winners_1_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_2 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_2 のチャットで待機してください')
        if message.channel.name == '1_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_2 のチャットで待機してください')
        if message.channel.name == 'winners_1_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_2 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_2 のチャットで待機してください')
        if message.channel.name == '1_5':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_3 のチャットで待機してください')
        if message.channel.name == 'winners_1_5':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_3 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_3 のチャットで待機してください')
        if message.channel.name == '1_6':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_3 のチャットで待機してください')
        if message.channel.name == 'winners_1_6':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_3 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_3 のチャットで待機してください')
        if message.channel.name == '1_7':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_4 のチャットで待機してください')
        if message.channel.name == 'winners_1_7':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_4 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_4 のチャットで待機してください')
        if message.channel.name == '1_8':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_4 のチャットで待機してください')
        if message.channel.name == 'winners_1_8':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_4 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_4 のチャットで待機してください')
        if message.channel.name == '1_9':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_5 のチャットで待機してください')
        if message.channel.name == 'winners_1_9':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_5 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_5 のチャットで待機してください')
        if message.channel.name == '1_10':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_5 のチャットで待機してください')
        if message.channel.name == 'winners_1_10':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_5 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_5 のチャットで待機してください')
        if message.channel.name == '1_11':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_6 のチャットで待機してください')
        if message.channel.name == 'winners_1_11':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_6 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_6 のチャットで待機してください')
        if message.channel.name == '1_12':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_6 のチャットで待機してください')
        if message.channel.name == 'winners_1_12':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_6 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_6 のチャットで待機してください')
        if message.channel.name == '1_13':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_7 のチャットで待機してください')
        if message.channel.name == 'winners_1_13':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_7 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_7 のチャットで待機してください')
        if message.channel.name == '1_14':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_7 のチャットで待機してください')
        if message.channel.name == 'winners_1_14':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_7 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_7 のチャットで待機してください')
        if message.channel.name == '1_15':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_8 のチャットで待機してください')
        if message.channel.name == 'winners_1_15':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_8 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_8 のチャットで待機してください')
        if message.channel.name == '1_16':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_8 のチャットで待機してください')
        if message.channel.name == 'winners_1_16':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_8 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_8 のチャットで待機してください')
        if message.channel.name == '1_17':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_9 のチャットで待機してください')
        if message.channel.name == 'winners_1_17':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_9 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_9 のチャットで待機してください')
        if message.channel.name == '1_18':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_9 のチャットで待機してください')
        if message.channel.name == 'winners_1_18':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_9 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_9 のチャットで待機してください')
        if message.channel.name == '1_19':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_10 のチャットで待機してください')
        if message.channel.name == 'winners_1_19':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_10 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_10 のチャットで待機してください')
        if message.channel.name == '1_20':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_10 のチャットで待機してください')
        if message.channel.name == 'winners_1_20':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_10 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_10 のチャットで待機してください')
        if message.channel.name == '1_21':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_11 のチャットで待機してください')
        if message.channel.name == 'winners_1_21':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_11 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_11 のチャットで待機してください')
        if message.channel.name == '1_22':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_11 のチャットで待機してください')
        if message.channel.name == 'winners_1_22':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_11 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_11 のチャットで待機してください')
        if message.channel.name == '1_23':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_12 のチャットで待機してください')
        if message.channel.name == 'winners_1_23':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_12 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_12 のチャットで待機してください')
        if message.channel.name == '1_24':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_12 のチャットで待機してください')
        if message.channel.name == 'winners_1_24':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_12 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_12 のチャットで待機してください')
        if message.channel.name == '1_25':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_13 のチャットで待機してください')
        if message.channel.name == 'winners_1_25':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_13 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_13 のチャットで待機してください')
        if message.channel.name == '1_26':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_13 のチャットで待機してください')
        if message.channel.name == 'winners_1_26':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_13 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_13 のチャットで待機してください')
        if message.channel.name == '1_27':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_14 のチャットで待機してください')
        if message.channel.name == 'winners_1_27':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_13 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_13 のチャットで待機してください')
        if message.channel.name == '1_28':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_14 のチャットで待機してください')
        if message.channel.name == 'winners_1_28':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_14 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_14 のチャットで待機してください')
        if message.channel.name == '1_29':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_15 のチャットで待機してください')
        if message.channel.name == 'winners_1_29':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_15 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_15 のチャットで待機してください')
        if message.channel.name == '1_30':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_15 のチャットで待機してください')
        if message.channel.name == 'winners_1_30':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_15 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_15 のチャットで待機してください')
        if message.channel.name == '1_31':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_16 のチャットで待機してください')
        if message.channel.name == 'winners_1_31':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_16 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_16 のチャットで待機してください')
        if message.channel.name == '1_32':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_16 のチャットで待機してください')
        if message.channel.name == 'winners_1_32':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_16 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_16 のチャットで待機してください')
        if message.channel.name == '1_33':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_17 のチャットで待機してください')
        if message.channel.name == 'winners_1_33':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_17 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_17 のチャットで待機してください')
        if message.channel.name == '1_34':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_17 のチャットで待機してください')
        if message.channel.name == 'winners_1_34':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_17 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_17 のチャットで待機してください')
        if message.channel.name == '1_35':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_18 のチャットで待機してください')
        if message.channel.name == 'winners_1_35':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_18 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_18 のチャットで待機してください')
        if message.channel.name == '1_36':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_18 のチャットで待機してください')
        if message.channel.name == 'winners_1_36':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_18 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_18 のチャットで待機してください')
        if message.channel.name == '1_37':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_19 のチャットで待機してください')
        if message.channel.name == 'winners_1_37':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_19 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_19 のチャットで待機してください')
        if message.channel.name == '1_38':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_19 のチャットで待機してください')
        if message.channel.name == 'winners_1_38':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_19 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_19 のチャットで待機してください')
        if message.channel.name == '1_39':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_20 のチャットで待機してください')
        if message.channel.name == 'winners_1_39':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_20 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_20 のチャットで待機してください')
        if message.channel.name == '1_40':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_20 のチャットで待機してください')
        if message.channel.name == 'winners_1_40':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_20 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_20 のチャットで待機してください')
        if message.channel.name == '1_41':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_21 のチャットで待機してください')
        if message.channel.name == 'winners_1_41':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_21 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_21 のチャットで待機してください')
        if message.channel.name == '1_42':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_21 のチャットで待機してください')
        if message.channel.name == 'winners_1_42':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_21 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_21 のチャットで待機してください')
        if message.channel.name == '1_43':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_22 のチャットで待機してください')
        if message.channel.name == 'winners_1_43':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_22 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_22 のチャットで待機してください')
        if message.channel.name == '1_44':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_22 のチャットで待機してください')
        if message.channel.name == 'winners_1_44':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_22 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_22 のチャットで待機してください')
        if message.channel.name == '1_45':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_23 のチャットで待機してください')
        if message.channel.name == 'winners_1_45':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_23 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_23 のチャットで待機してください')
        if message.channel.name == '1_46':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_23 のチャットで待機してください')
        if message.channel.name == 'winners_1_46':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_23 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_23 のチャットで待機してください')
        if message.channel.name == '1_47':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_24 のチャットで待機してください')
        if message.channel.name == 'winners_1_47':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_24 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_24 のチャットで待機してください')
        if message.channel.name == '1_48':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_24 のチャットで待機してください')
        if message.channel.name == 'winners_1_48':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_24 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_24 のチャットで待機してください')
        if message.channel.name == '1_49':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_25 のチャットで待機してください')
        if message.channel.name == 'winners_1_49':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_25 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_25 のチャットで待機してください')
        if message.channel.name == '1_50':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_25 のチャットで待機してください')
        if message.channel.name == 'winners_1_50':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_26 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_26 のチャットで待機してください')
        if message.channel.name == '1_51':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_26 のチャットで待機してください')
        if message.channel.name == 'winners_1_51':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_26 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_26 のチャットで待機してください')
        if message.channel.name == '1_52':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_26 のチャットで待機してください')
        if message.channel.name == 'winners_1_52':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_26 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_26 のチャットで待機してください')
        if message.channel.name == '1_53':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_27 のチャットで待機してください')
        if message.channel.name == 'winners_1_53':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_27 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_27 のチャットで待機してください')
        if message.channel.name == '1_54':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_27 のチャットで待機してください')
        if message.channel.name == 'winners_1_54':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_27 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_27 のチャットで待機してください')
        if message.channel.name == '1_55':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_28 のチャットで待機してください')
        if message.channel.name == 'winners_1_55':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_28 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_28 のチャットで待機してください')
        if message.channel.name == '1_56':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_28 のチャットで待機してください')
        if message.channel.name == 'winners_1_56':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_28 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_28 のチャットで待機してください')
        if message.channel.name == '1_57':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_29 のチャットで待機してください')
        if message.channel.name == 'winners_1_57':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_29 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_29 のチャットで待機してください')
        if message.channel.name == '1_58':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_29 のチャットで待機してください')
        if message.channel.name == 'winners_1_58':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_29 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_29 のチャットで待機してください')
        if message.channel.name == '1_59':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_30 のチャットで待機してください')
        if message.channel.name == 'winners_1_59':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_30 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_30 のチャットで待機してください')
        if message.channel.name == '1_60':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_30 のチャットで待機してください')
        if message.channel.name == 'winners_1_60':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_30 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_30 のチャットで待機してください')
        if message.channel.name == '1_61':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_31 のチャットで待機してください')
        if message.channel.name == 'winners_1_61':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_31 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_31 のチャットで待機してください')
        if message.channel.name == '1_62':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_31 のチャットで待機してください')
        if message.channel.name == 'winners_1_62':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_31 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_31 のチャットで待機してください')
        if message.channel.name == '1_63':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_32 のチャットで待機してください')
        if message.channel.name == 'winners_1_63':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_32 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_32 のチャットで待機してください')
        if message.channel.name == '1_64':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_32 のチャットで待機してください')
        if message.channel.name == 'winners_1_64':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_32 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_32 のチャットで待機してください')
        if message.channel.name == '1_65':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_33 のチャットで待機してください')
        if message.channel.name == 'winners_1_65':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_33 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_33 のチャットで待機してください')
        if message.channel.name == '1_66':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_33 のチャットで待機してください')
        if message.channel.name == 'winners_1_66':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_33 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_33 のチャットで待機してください')
        if message.channel.name == '1_67':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_34 のチャットで待機してください')
        if message.channel.name == 'winners_1_67':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_34 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_34 のチャットで待機してください')
        if message.channel.name == '1_68':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_34 のチャットで待機してください')
        if message.channel.name == 'winners_1_68':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_34 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_34 のチャットで待機してください')
        if message.channel.name == '1_69':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_35 のチャットで待機してください')
        if message.channel.name == 'winners_1_69':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_35 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_35 のチャットで待機してください')
        if message.channel.name == '1_70':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_35 のチャットで待機してください')
        if message.channel.name == 'winners_1_70':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_35 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_35 のチャットで待機してください')
        if message.channel.name == '1_71':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_36 のチャットで待機してください')
        if message.channel.name == 'winners_1_71':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_36 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_36 のチャットで待機してください')
        if message.channel.name == '1_72':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_36 のチャットで待機してください')
        if message.channel.name == 'winners_1_72':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_36 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_36 のチャットで待機してください')
        if message.channel.name == '1_73':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_37 のチャットで待機してください')
        if message.channel.name == 'winners_1_73':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_37 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_37 のチャットで待機してください')
        if message.channel.name == '1_74':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_37 のチャットで待機してください')
        if message.channel.name == 'winners_1_74':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_37 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_37 のチャットで待機してください')
        if message.channel.name == '1_75':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_38 のチャットで待機してください')
        if message.channel.name == 'winners_1_75':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_38 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_38 のチャットで待機してください')
        if message.channel.name == '1_76':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_38 のチャットで待機してください')
        if message.channel.name == 'winners_1_76':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_38 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_38 のチャットで待機してください')
        if message.channel.name == '1_77':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_39 のチャットで待機してください')
        if message.channel.name == 'winners_1_77':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_39 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_39 のチャットで待機してください')
        if message.channel.name == '1_78':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_39 のチャットで待機してください')
        if message.channel.name == 'winners_1_78':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_39 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_39 のチャットで待機してください')
        if message.channel.name == '1_79':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_40 のチャットで待機してください')
        if message.channel.name == 'winners_1_78':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_40 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_40 のチャットで待機してください')
        if message.channel.name == '1_80':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_40 のチャットで待機してください')
        if message.channel.name == 'winners_1_80':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_40 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_40 のチャットで待機してください')
        if message.channel.name == '1_81':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_41 のチャットで待機してください')
        if message.channel.name == 'winners_1_81':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_41 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_41 のチャットで待機してください')
        if message.channel.name == '1_82':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_41 のチャットで待機してください')
        if message.channel.name == 'winners_1_82':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_41 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_41 のチャットで待機してください')
        if message.channel.name == '1_83':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_42 のチャットで待機してください')
        if message.channel.name == 'winners_1_83':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_42 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_42 のチャットで待機してください')
        if message.channel.name == '1_84':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_42 のチャットで待機してください')
        if message.channel.name == 'winners_1_84':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_42 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_42 のチャットで待機してください')
        if message.channel.name == '1_85':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_43 のチャットで待機してください')
        if message.channel.name == 'winners_1_85':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_43 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_43 のチャットで待機してください')
        if message.channel.name == '1_86':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_43 のチャットで待機してください')
        if message.channel.name == 'winners_1_86':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_43 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_43 のチャットで待機してください')
        if message.channel.name == '1_87':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_44 のチャットで待機してください')
        if message.channel.name == 'winners_1_87':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_44 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_44 のチャットで待機してください')
        if message.channel.name == '1_88':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_44 のチャットで待機してください')
        if message.channel.name == 'winners_1_88':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_44 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_44 のチャットで待機してください')
        if message.channel.name == '1_89':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_45 のチャットで待機してください')
        if message.channel.name == 'winners_1_89':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_45 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_45 のチャットで待機してください')
        if message.channel.name == '1_90':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_45 のチャットで待機してください')
        if message.channel.name == 'winners_1_90':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_45 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_45 のチャットで待機してください')
        if message.channel.name == '1_91':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_46 のチャットで待機してください')
        if message.channel.name == 'winners_1_91':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_46 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_46 のチャットで待機してください')
        if message.channel.name == '1_92':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_46 のチャットで待機してください')
        if message.channel.name == 'winners_1_92':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_46 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_46 のチャットで待機してください')
        if message.channel.name == '1_93':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_47 のチャットで待機してください')
        if message.channel.name == 'winners_1_93':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_47 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_47 のチャットで待機してください')
        if message.channel.name == '1_94':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_47 のチャットで待機してください')
        if message.channel.name == 'winners_1_94':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_47 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_47 のチャットで待機してください')
        if message.channel.name == '1_95':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_48 のチャットで待機してください')
        if message.channel.name == 'winners_1_95':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_48 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_48 のチャットで待機してください')
        if message.channel.name == '1_96':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_48 のチャットで待機してください')
        if message.channel.name == 'winners_1_96':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_48 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_48 のチャットで待機してください')
        if message.channel.name == '1_97':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_49 のチャットで待機してください')
        if message.channel.name == 'winners_1_97':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_49 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_49 のチャットで待機してください')
        if message.channel.name == '1_98':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_49 のチャットで待機してください')
        if message.channel.name == 'winners_1_98':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_49 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_49 のチャットで待機してください')
        if message.channel.name == '1_99':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_50 のチャットで待機してください')
        if message.channel.name == 'winners_1_99':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_50 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_50 のチャットで待機してください')
        if message.channel.name == '1_100':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_50 のチャットで待機してください')
        if message.channel.name == 'winners_1_100':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_50 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_50 のチャットで待機してください')
        if message.channel.name == '1_101':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_51 のチャットで待機してください')
        if message.channel.name == 'winners_1_101':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_51 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_51 のチャットで待機してください')
        if message.channel.name == '1_102':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_51 のチャットで待機してください')
        if message.channel.name == 'winners_1_102':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_51 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_51 のチャットで待機してください')
        if message.channel.name == '1_103':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_52 のチャットで待機してください')
        if message.channel.name == 'winners_1_103':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_52 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_52 のチャットで待機してください')
        if message.channel.name == '1_104':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_52 のチャットで待機してください')
        if message.channel.name == 'winners_1_104':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_52 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_52 のチャットで待機してください')
        if message.channel.name == '1_105':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_53 のチャットで待機してください')
        if message.channel.name == 'winners_1_105':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_53 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_53 のチャットで待機してください')
        if message.channel.name == '1_106':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_53 のチャットで待機してください')
        if message.channel.name == 'winners_1_106':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_53 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_53 のチャットで待機してください')
        if message.channel.name == '1_107':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_54 のチャットで待機してください')
        if message.channel.name == 'winners_1_107':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_54 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_54 のチャットで待機してください')
        if message.channel.name == '1_108':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_54 のチャットで待機してください')
        if message.channel.name == 'winners_1_108':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_54 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_54 のチャットで待機してください')
        if message.channel.name == '1_109':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_55 のチャットで待機してください')
        if message.channel.name == 'winners_1_109':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_55 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_55 のチャットで待機してください')
        if message.channel.name == '1_110':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_55 のチャットで待機してください')
        if message.channel.name == 'winners_1_110':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_55 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_55 のチャットで待機してください')
        if message.channel.name == '1_111':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_56 のチャットで待機してください')
        if message.channel.name == 'winners_1_111':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_56 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_56 のチャットで待機してください')
        if message.channel.name == '1_112':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_56 のチャットで待機してください')
        if message.channel.name == 'winners_1_112':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_56 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_56 のチャットで待機してください')
        if message.channel.name == '1_113':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_57 のチャットで待機してください')
        if message.channel.name == 'winners_1_113':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_57 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_57 のチャットで待機してください')
        if message.channel.name == '1_114':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_57 のチャットで待機してください')
        if message.channel.name == 'winners_1_114':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_57 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_57 のチャットで待機してください')
        if message.channel.name == '1_115':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_58 のチャットで待機してください')
        if message.channel.name == 'winners_1_115':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_58 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_58 のチャットで待機してください')
        if message.channel.name == '1_116':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_58 のチャットで待機してください')
        if message.channel.name == 'winners_1_116':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_58 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_58 のチャットで待機してください')
        if message.channel.name == '1_117':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_59 のチャットで待機してください')
        if message.channel.name == 'winners_1_117':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_59 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_59 のチャットで待機してください')
        if message.channel.name == '1_118':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_59 のチャットで待機してください')
        if message.channel.name == 'winners_1_118':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_59 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_59 のチャットで待機してください')
        if message.channel.name == '1_119':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_60 のチャットで待機してください')
        if message.channel.name == 'winners_1_119':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_60 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_60 のチャットで待機してください')
        if message.channel.name == '1_120':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_60 のチャットで待機してください')
        if message.channel.name == 'winners_1_120':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_60 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_60 のチャットで待機してください')
        if message.channel.name == '1_121':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_61 のチャットで待機してください')
        if message.channel.name == 'winners_1_121':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_61 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_61 のチャットで待機してください')
        if message.channel.name == '1_122':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_61 のチャットで待機してください')
        if message.channel.name == 'winners_1_122':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_61 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_61 のチャットで待機してください')
        if message.channel.name == '1_123':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_62 のチャットで待機してください')
        if message.channel.name == 'winners_1_123':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_62 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_62 のチャットで待機してください')
        if message.channel.name == '1_124':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_62 のチャットで待機してください')
        if message.channel.name == 'winners_1_124':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_62 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_62 のチャットで待機してください')
        if message.channel.name == '1_125':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_63 のチャットで待機してください')
        if message.channel.name == 'winners_1_125':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_63 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_63 のチャットで待機してください')
        if message.channel.name == '1_126':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_63 のチャットで待機してください')
        if message.channel.name == 'winners_1_126':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_63 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_63 のチャットで待機してください')
        if message.channel.name == '1_127':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_64 のチャットで待機してください')
        if message.channel.name == 'winners_1_127':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_64 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_64 のチャットで待機してください')
        if message.channel.name == '1_128':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #2_64 のチャットで待機してください')
        if message.channel.name == 'winners_1_128':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_2_64 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_1_64 のチャットで待機してください')

        # ここから２回戦の誘導

        if message.channel.name == '2_1':
            try:
                j = l.index('3_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_1 のチャットで待機してください')
                #losers_2_3
        if message.channel.name == '2_2':
            try:
                j = l.index('3_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_1 のチャットで待機してください')
        if message.channel.name == '2_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_2 のチャットで待機してください')
        if message.channel.name == '2_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_2 のチャットで待機してください')
        if message.channel.name == '2_5':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_3 のチャットで待機してください')
        if message.channel.name == '2_6':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_3 のチャットで待機してください')
        if message.channel.name == '2_7':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_4 のチャットで待機してください')
        if message.channel.name == '2_8':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_4 のチャットで待機してください')
        if message.channel.name == '2_9':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_5 のチャットで待機してください')
        if message.channel.name == '2_10':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_5 のチャットで待機してください')
        if message.channel.name == '2_11':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_6 のチャットで待機してください')
        if message.channel.name == '2_12':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_6 のチャットで待機してください')
        if message.channel.name == '2_13':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_7 のチャットで待機してください')
        if message.channel.name == '2_14':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_7 のチャットで待機してください')
        if message.channel.name == '2_15':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_8 のチャットで待機してください')
        if message.channel.name == '2_16':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_8 のチャットで待機してください')
        if message.channel.name == '2_17':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_9 のチャットで待機してください')
        if message.channel.name == '2_18':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_9 のチャットで待機してください')
        if message.channel.name == '2_19':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_10 のチャットで待機してください')
        if message.channel.name == '2_20':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_10 のチャットで待機してください')
        if message.channel.name == '2_21':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_11 のチャットで待機してください')
        if message.channel.name == '2_22':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_11 のチャットで待機してください')
        if message.channel.name == '2_23':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_12 のチャットで待機してください')
        if message.channel.name == '2_24':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_12 のチャットで待機してください')
        if message.channel.name == '2_25':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_13 のチャットで待機してください')
        if message.channel.name == '2_26':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_13 のチャットで待機してください')
        if message.channel.name == '2_27':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_14 のチャットで待機してください')
        if message.channel.name == '2_28':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_14 のチャットで待機してください')
        if message.channel.name == '2_29':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_15 のチャットで待機してください')
        if message.channel.name == '2_30':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_15 のチャットで待機してください')
        if message.channel.name == '2_31':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_16 のチャットで待機してください')
        if message.channel.name == '2_32':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_16 のチャットで待機してください')
        if message.channel.name == '2_33':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_17 のチャットで待機してください')
        if message.channel.name == '2_34':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_17 のチャットで待機してください')
        if message.channel.name == '2_35':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_18 のチャットで待機してください')
        if message.channel.name == '2_36':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_18 のチャットで待機してください')
        if message.channel.name == '2_37':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_19 のチャットで待機してください')
        if message.channel.name == '2_38':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_19 のチャットで待機してください')
        if message.channel.name == '2_39':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_20 のチャットで待機してください')
        if message.channel.name == '2_40':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_20 のチャットで待機してください')
        if message.channel.name == '2_41':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_21 のチャットで待機してください')
        if message.channel.name == '2_42':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_21 のチャットで待機してください')
        if message.channel.name == '2_42':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_22 のチャットで待機してください')
        if message.channel.name == '2_44':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_22 のチャットで待機してください')
        if message.channel.name == '2_45':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_23 のチャットで待機してください')
        if message.channel.name == '2_46':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_23 のチャットで待機してください')
        if message.channel.name == '2_47':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_24 のチャットで待機してください')
        if message.channel.name == '2_48':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_24 のチャットで待機してください')
        if message.channel.name == '2_49':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_25 のチャットで待機してください')
        if message.channel.name == '2_50':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_25 のチャットで待機してください')
        if message.channel.name == '2_51':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_26 のチャットで待機してください')
        if message.channel.name == '2_52':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_26 のチャットで待機してください')
        if message.channel.name == '2_53':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_27 のチャットで待機してください')
        if message.channel.name == '2_54':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_27 のチャットで待機してください')
        if message.channel.name == '2_55':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_28 のチャットで待機してください')
        if message.channel.name == '2_56':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_28 のチャットで待機してください')
        if message.channel.name == '2_57':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_29 のチャットで待機してください')
        if message.channel.name == '2_58':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_29 のチャットで待機してください')
        if message.channel.name == '2_59':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_30 のチャットで待機してください')
        if message.channel.name == '2_60':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_30 のチャットで待機してください')
        if message.channel.name == '2_61':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_31 のチャットで待機してください')
        if message.channel.name == '2_62':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_31 のチャットで待機してください')
        if message.channel.name == '2_63':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_32 のチャットで待機してください')
        if message.channel.name == '2_64':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #3_32 のチャットで待機してください')

#ここから三回戦
        if message.channel.name == '3_1':
            try:
                j = l.index('4_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_1 のチャットで待機してください')
        if message.channel.name == '3_2':
            try:
                j = l.index('4_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_1 のチャットで待機してください')
        if message.channel.name == '3_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_2 のチャットで待機してください')
        if message.channel.name == '3_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_2 のチャットで待機してください')
        if message.channel.name == '3_5':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_3 のチャットで待機してください')
        if message.channel.name == '3_6':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_3 のチャットで待機してください')
        if message.channel.name == '3_7':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_4 のチャットで待機してください')
        if message.channel.name == '3_8':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_4 のチャットで待機してください')
        if message.channel.name == '3_9':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_5 のチャットで待機してください')
        if message.channel.name == '3_10':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_5 のチャットで待機してください')
        if message.channel.name == '3_11':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_6 のチャットで待機してください')
        if message.channel.name == '3_12':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_6 のチャットで待機してください')
        if message.channel.name == '3_13':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_7 のチャットで待機してください')
        if message.channel.name == '3_14':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_7 のチャットで待機してください')
        if message.channel.name == '3_15':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_8 のチャットで待機してください')
        if message.channel.name == '3_16':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_8 のチャットで待機してください')
        if message.channel.name == '3_17':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_9 のチャットで待機してください')
        if message.channel.name == '3_18':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_9 のチャットで待機してください')
        if message.channel.name == '3_19':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_10 のチャットで待機してください')
        if message.channel.name == '3_20':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_10 のチャットで待機してください')
        if message.channel.name == '3_21':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_11 のチャットで待機してください')
        if message.channel.name == '3_22':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_11 のチャットで待機してください')
        if message.channel.name == '3_23':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_12 のチャットで待機してください')
        if message.channel.name == '3_24':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_12 のチャットで待機してください')
        if message.channel.name == '3_25':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_13 のチャットで待機してください')
        if message.channel.name == '3_26':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_13 のチャットで待機してください')
        if message.channel.name == '3_27':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_14 のチャットで待機してください')
        if message.channel.name == '3_28':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_14 のチャットで待機してください')
        if message.channel.name == '3_29':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_15 のチャットで待機してください')
        if message.channel.name == '3_30':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_15 のチャットで待機してください')
        if message.channel.name == '3_31':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_16 のチャットで待機してください')
        if message.channel.name == '3_32':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #4_16 のチャットで待機してください')

#ここから４回戦の誘導
        if message.channel.name == '4_1':
            try:
                j = l.index('5_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #5_1 のチャットで待機してください')
        if message.channel.name == '4_2':
            try:
                j = l.index('5_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #5_1 のチャットで待機してください')
        if message.channel.name == '4_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #5_2 のチャットで待機してください')
        if message.channel.name == '4_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #5_2 のチャットで待機してください')
        if message.channel.name == '4_5':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #5_3 のチャットで待機してください')
        if message.channel.name == '4_6':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #5_3 のチャットで待機してください')
        if message.channel.name == '4_7':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #5_4 のチャットで待機してください')
        if message.channel.name == '4_8':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #5_4 のチャットで待機してください')
        if message.channel.name == '4_9':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #5_5 のチャットで待機してください')
        if message.channel.name == '4_10':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #5_5 のチャットで待機してください')
        if message.channel.name == '4_11':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #5_6 のチャットで待機してください')
        if message.channel.name == '4_12':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #5_6 のチャットで待機してください')
        if message.channel.name == '4_13':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #5_7 のチャットで待機してください')
        if message.channel.name == '4_14':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #5_7 のチャットで待機してください')
        if message.channel.name == '4_15':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #5_8 のチャットで待機してください')
        if message.channel.name == '4_16':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #5_8 のチャットで待機してください')
#ここから５回戦の誘導
        if message.channel.name == '5_1':
            try:
                j = l.index('6_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #6_1 のチャットで待機してください')
        if message.channel.name == '5_2':
            try:
                j = l.index('6_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #6_1 のチャットで待機してください')
        if message.channel.name == '5_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #6_2 のチャットで待機してください')
        if message.channel.name == '5_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #6_2 のチャットで待機してください')
        if message.channel.name == '5_5':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #6_3 のチャットで待機してください')
        if message.channel.name == '5_6':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #6_3 のチャットで待機してください')
        if message.channel.name == '5_7':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #6_4 のチャットで待機してください')
        if message.channel.name == '5_8':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #6_4 のチャットで待機してください')

#ここから６回戦の誘導
        if message.channel.name == '6_1':
            try:
                j = l.index('7_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #7_1 のチャットで待機してください')
        if message.channel.name == '6_2':
            try:
                j = l.index('7_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #7_1 のチャットで待機してください')
        if message.channel.name == '6_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #7_2 のチャットで待機してください')
        if message.channel.name == '6_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #7_2 のチャットで待機してください')

#ここから７回戦の誘導
        if message.channel.name == '7_1':
            try:
                j = l.index('8_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #8_1 のチャットで待機してください')
        if message.channel.name == '7_2':
            try:
                j = l.index('8_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #8_1 のチャットで待機してください')
#ここからfinal
        if message.channel.name == 'final':
            await client.send_message(message.channel, 'Congratulations!!! 優勝おめでとうございます!!')

#ダブルイリミネーションwinners


        if message.channel.name == 'winners_2_1':
            try:
                j = l.index('winners_3_1')
                s = l.index('winners_4_1')
                i = l.index('winners_5_1')
                p = l.index('winners_6_1')
                n = l.index('winners_7_1')


            except ValueError:
                j = None
                s = None
                i = None
                p = None
                n = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_final のチャットで待機してください')
                await client.send_message(message.channel, '敗北チームは #losers_2_2 のチャットで待機してください')
                print(s)
                print(i)
                print(p)
                print(n)
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_1 のチャットで待機してください')
                await client.send_message(message.channel, '敗北チームは #losers_2_4 のチャットで待機してください')
        if message.channel.name == 'winners_2_2':
            try:
                j = l.index('winners_3_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_final のチャットで待機してください')
                await client.send_message(message.channel, '敗北チームは #losers_2_1 のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_1 のチャットで待機してください')
                await client.send_message(message.channel, '敗者チームは #losers_2_1 のチャットで待機してください')

        if message.channel.name == 'winners_2_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_2 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_3 のチャットで待機してください')
        if message.channel.name == 'winners_2_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_2 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_4 のチャットで待機してください')
        if message.channel.name == 'winners_2_5':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_3 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_6 のチャットで待機してください')
        if message.channel.name == 'winners_2_6':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_3 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_6 のチャットで待機してください')
        if message.channel.name == 'winners_2_7':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_4 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_7 のチャットで待機してください')
        if message.channel.name == 'winners_2_8':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_4 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_8 のチャットで待機してください')
        if message.channel.name == 'winners_2_9':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_5 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_9 のチャットで待機してください')
        if message.channel.name == 'winners_2_10':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_5 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_10 のチャットで待機してください')
        if message.channel.name == 'winners_2_11':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_6 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_11 のチャットで待機してください')
        if message.channel.name == 'winners_2_12':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_6 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_12 のチャットで待機してください')
        if message.channel.name == 'winners_2_13':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_7 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_13 のチャットで待機してください')
        if message.channel.name == 'winners_2_14':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_7 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_14 のチャットで待機してください')
        if message.channel.name == 'winners_2_15':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_8 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_15 のチャットで待機してください')
        if message.channel.name == 'winners_2_16':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_8 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_16 のチャットで待機してください')
        if message.channel.name == 'winners_2_17':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_9 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_17 のチャットで待機してください')
        if message.channel.name == 'winners_2_18':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_9 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_18 のチャットで待機してください')
        if message.channel.name == 'winners_2_19':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_10 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_19 のチャットで待機してください')
        if message.channel.name == 'winners_2_20':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_10 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_20 のチャットで待機してください')
        if message.channel.name == 'winners_2_21':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_11 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_21 のチャットで待機してください')
        if message.channel.name == 'winners_2_22':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_11 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_22 のチャットで待機してください')
        if message.channel.name == 'winners_2_23':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_12 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_23 のチャットで待機してください')
        if message.channel.name == 'winners_2_24':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_12 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_24 のチャットで待機してください')
        if message.channel.name == 'winners_2_25':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_13 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_25 のチャットで待機してください')
        if message.channel.name == 'winners_2_26':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_13 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_26 のチャットで待機してください')
        if message.channel.name == 'winners_2_27':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_14 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_27 のチャットで待機してください')
        if message.channel.name == 'winners_2_28':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_14 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_28 のチャットで待機してください')
        if message.channel.name == 'winners_2_29':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_15 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_29 のチャットで待機してください')
        if message.channel.name == 'winners_2_30':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_15 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_30 のチャットで待機してください')
        if message.channel.name == 'winners_2_31':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_16 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_31 のチャットで待機してください')
        if message.channel.name == 'winners_2_32':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_16 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_32 のチャットで待機してください')
        if message.channel.name == 'winners_2_33':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_17 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_33 のチャットで待機してください')
        if message.channel.name == 'winners_2_34':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_17 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_34 のチャットで待機してください')
        if message.channel.name == 'winners_2_35':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_18 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_35 のチャットで待機してください')
        if message.channel.name == 'winners_2_36':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_18 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_36 のチャットで待機してください')
        if message.channel.name == 'winners_2_37':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_19 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_37 のチャットで待機してください')
        if message.channel.name == 'winners_2_38':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_19 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_38 のチャットで待機してください')
        if message.channel.name == 'winners_2_39':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_20 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_39 のチャットで待機してください')
        if message.channel.name == 'winners_2_40':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_20 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_40 のチャットで待機してください')
        if message.channel.name == 'winners_2_41':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_21 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_41 のチャットで待機してください')
        if message.channel.name == 'winners_2_42':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_21 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_42 のチャットで待機してください')
        if message.channel.name == 'winners_2_42':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_22 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_43 のチャットで待機してください')
        if message.channel.name == 'winners_2_44':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_22 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_44 のチャットで待機してください')
        if message.channel.name == 'winners_2_45':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_23 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_45 のチャットで待機してください')
        if message.channel.name == 'winners_2_46':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_23 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_46 のチャットで待機してください')
        if message.channel.name == 'winners_2_47':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_24 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_47 のチャットで待機してください')
        if message.channel.name == 'winners_2_48':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_24 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_48 のチャットで待機してください')
        if message.channel.name == 'winners_2_49':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_25 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_49 のチャットで待機してください')
        if message.channel.name == 'winners_2_50':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_25 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_50 のチャットで待機してください')
        if message.channel.name == 'winners_2_51':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_26 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_51 のチャットで待機してください')
        if message.channel.name == 'winners_2_52':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_26 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_52 のチャットで待機してください')
        if message.channel.name == 'winners_2_53':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_27 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_53 のチャットで待機してください')
        if message.channel.name == 'winners_2_54':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_27 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_54 のチャットで待機してください')
        if message.channel.name == 'winners_2_55':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_28 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_55 のチャットで待機してください')
        if message.channel.name == 'winners_2_56':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_28 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_56 のチャットで待機してください')
        if message.channel.name == 'winners_2_57':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_29 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_57 のチャットで待機してください')
        if message.channel.name == 'winners_2_58':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_29 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_58 のチャットで待機してください')
        if message.channel.name == 'winners_2_59':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_30 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_59 のチャットで待機してください')
        if message.channel.name == 'winners_2_60':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_30 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_60 のチャットで待機してください')
        if message.channel.name == 'winners_2_61':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_31 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_61 のチャットで待機してください')
        if message.channel.name == 'winners_2_62':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_31 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_62 のチャットで待機してください')
        if message.channel.name == 'winners_2_63':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_32 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_63 のチャットで待機してください')
        if message.channel.name == 'winners_2_64':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_3_32 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_2_64 のチャットで待機してください')
#winners3回線
        if message.channel.name == 'winners_3_1':
            try:
                j = l.index('winners_4_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_final のチャットで待機してください')
                await client.send_message(message.channel, '敗北チームは #losers_4_1 のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_1 のチャットで待機してください')
                await client.send_message(message.channel, '敗者チームは #losers_4_1 のチャットで待機してください')
        if message.channel.name == 'winners_3_2':
            try:
                j = l.index('winners_4_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_final のチャットで待機してください')
                await client.send_message(message.channel, '敗北チームは #losers_4_2 のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_1 のチャットで待機してください')
                await client.send_message(message.channel, '敗者チームは #losers_4_2 のチャットで待機してください')

        if message.channel.name == 'winners_3_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_2 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_3 のチャットで待機してください')
        if message.channel.name == 'winners_3_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_2 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_4 のチャットで待機してください')
        if message.channel.name == 'winners_3_5':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_3 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_5 のチャットで待機してください')
        if message.channel.name == 'winners_3_6':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_3 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_6 のチャットで待機してください')
        if message.channel.name == 'winners_3_7':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_4 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_7 のチャットで待機してください')
        if message.channel.name == 'winners_3_8':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_4 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_8 のチャットで待機してください')
        if message.channel.name == 'winners_3_9':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_5 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_9 のチャットで待機してください')
        if message.channel.name == 'winners_3_10':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_5 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_10 のチャットで待機してください')
        if message.channel.name == 'winners_3_11':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_6 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_11 のチャットで待機してください')
        if message.channel.name == 'winners_3_12':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_6 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_12 のチャットで待機してください')
        if message.channel.name == 'winners_3_13':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_7 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_13 のチャットで待機してください')
        if message.channel.name == 'winners_3_14':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_7 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_14 のチャットで待機してください')
        if message.channel.name == 'winners_3_15':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_8 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_15 のチャットで待機してください')
        if message.channel.name == 'winners_3_16':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_8 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_16 のチャットで待機してください')
        if message.channel.name == 'winners_3_17':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_9 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_17 のチャットで待機してください')
        if message.channel.name == 'winners_3_18':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_9 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_18 のチャットで待機してください')
        if message.channel.name == 'winners_3_19':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_10 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_19 のチャットで待機してください')
        if message.channel.name == 'winners_3_20':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_10 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_20 のチャットで待機してください')
        if message.channel.name == 'winners_3_21':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_11 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_21 のチャットで待機してください')
        if message.channel.name == 'winners_3_22':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_11 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_22 のチャットで待機してください')
        if message.channel.name == 'winners_3_23':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_12 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_23 のチャットで待機してください')
        if message.channel.name == 'winners_3_24':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_12 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_24 のチャットで待機してください')
        if message.channel.name == 'winners_3_25':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_13 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_25 のチャットで待機してください')
        if message.channel.name == 'winners_3_26':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_13 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_26 のチャットで待機してください')
        if message.channel.name == 'winners_3_27':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_14 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_27 のチャットで待機してください')
        if message.channel.name == 'winners_3_28':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_14 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_28 のチャットで待機してください')
        if message.channel.name == 'winners_3_29':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_15 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_29 のチャットで待機してください')
        if message.channel.name == 'winners_3_30':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_15 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_30 のチャットで待機してください')
        if message.channel.name == 'winners_3_31':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_16 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_31 のチャットで待機してください')
        if message.channel.name == 'winners_3_32':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_4_16 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_4_32 のチャットで待機してください')


#winners 4回戦
        if message.channel.name == 'winners_4_1':
            try:
                j = l.index('winners_5_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_final のチャットで待機してください')
                await client.send_message(message.channel, '敗北チームは #losers_6_1 のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_5_1 のチャットで待機してください')
                await client.send_message(message.channel, '敗者チームは #losers_6_1 のチャットで待機してください')
        if message.channel.name == 'winners_4_2':
            try:
                j = l.index('winners_5_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_final のチャットで待機してください')
                await client.send_message(message.channel, '敗北チームは #losers_6_2 のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_5_1 のチャットで待機してください')
                await client.send_message(message.channel, '敗者チームは #losers_6_2 のチャットで待機してください')

        if message.channel.name == 'winners_4_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_5_2 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_6_3 のチャットで待機してください')
        if message.channel.name == 'winners_4_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_5_2 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_6_4 のチャットで待機してください')
        if message.channel.name == 'winners_4_5':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_5_3 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_6_5 のチャットで待機してください')
        if message.channel.name == 'winners_4_6':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_5_3 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_6_6 のチャットで待機してください')
        if message.channel.name == 'winners_4_7':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_5_4 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_6_7 のチャットで待機してください')
        if message.channel.name == 'winners_4_8':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_5_4 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_6_8 のチャットで待機してください')
        if message.channel.name == 'winners_4_9':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_5_5 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_6_9 のチャットで待機してください')
        if message.channel.name == 'winners_4_10':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_5_5 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_6_10 のチャットで待機してください')
        if message.channel.name == 'winners_4_11':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_5_6 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_6_11 のチャットで待機してください')
        if message.channel.name == 'winners_4_12':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_5_6 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_6_12 のチャットで待機してください')
        if message.channel.name == 'winners_4_13':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_5_7 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_6_13 のチャットで待機してください')
        if message.channel.name == 'winners_4_14':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_5_7 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_6_14 のチャットで待機してください')
        if message.channel.name == 'winners_4_15':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_5_8 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_6_15 のチャットで待機してください')
        if message.channel.name == 'winners_4_16':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_5_8 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_6_16 のチャットで待機してください')

#5回戦 winners
        if message.channel.name == 'winners_5_1':
            try:
                j = l.index('winners_6_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_final のチャットで待機してください')
                await client.send_message(message.channel, '敗者チームは #losers_8_1 のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_6_1 のチャットで待機してください')
                await client.send_message(message.channel, '敗者チームは #losers_8_1 のチャットで待機してください')
        if message.channel.name == 'winners_5_2':
            try:
                j = l.index('winners_6_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_final のチャットで待機してください')
                await client.send_message(message.channel, '敗者チームは #losers_8_2 のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_6_1 のチャットで待機してください')
                await client.send_message(message.channel, '敗者チームは #losers_8_2 のチャットで待機してください')
        if message.channel.name == 'winners_5_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_6_2 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_8_3 のチャットで待機してください')
        if message.channel.name == 'winners_5_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_6_2 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_8_4 のチャットで待機してください')
        if message.channel.name == 'winners_5_5':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_6_3 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_8_5 のチャットで待機してください')
        if message.channel.name == 'winners_5_6':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_6_3 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_8_6 のチャットで待機してください')
        if message.channel.name == 'winners_5_7':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_6_4 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_8_7 のチャットで待機してください')
        if message.channel.name == 'winners_5_8':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_6_4 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_8_8 のチャットで待機してください')
#6回戦 winners
        if message.channel.name == 'winners_6_1':
            try:
                j = l.index('winners_7_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_final のチャットで待機してください')
                await client.send_message(message.channel, '敗者チームは #losers_10_1 のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_7_1 のチャットで待機してください')
                await client.send_message(message.channel, '敗者チームは #losers_10_1 のチャットで待機してください')
        if message.channel.name == 'winners_6_2':
            try:
                j = l.index('winners_7_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_final のチャットで待機してください')
                await client.send_message(message.channel, '敗者チームは #losers_10_2 のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_7_1 のチャットで待機してください')
                await client.send_message(message.channel, '敗者チームは #losers_10_2 のチャットで待機してください')

        if message.channel.name == 'winners_6_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_7_2 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_10_3 のチャットで待機してください')
        if message.channel.name == 'winners_6_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_7_2 のチャットで待機してください')
            await client.send_message(message.channel, '敗者チームは #losers_10_4 のチャットで待機してください')

#ここから７回戦の誘導 winners
        if message.channel.name == 'winners_7_1':
            try:
                j = l.index('winners_8_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_final のチャットで待機してください')
                await client.send_message(message.channel, '敗者チームは #losers_12_1 のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_8_1 のチャットで待機してください')
                await client.send_message(message.channel, '敗者チームは #losers_12_1 のチャットで待機してください')
        if message.channel.name == 'winners_7_2':
            try:
                j = l.index('winners_8_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #winners_final のチャットで待機してください')
                await client.send_message(message.channel, '敗者チームは #losers_12_2 のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは winners_#8_1 のチャットで待機してください')
                await client.send_message(message.channel, '敗者チームは #losers_12_2 のチャットで待機してください')
#ここからfinal winners
        if message.channel.name == 'winners_final':
            await client.send_message(message.channel, 'Congratulations!!! winners優勝おめでとうございます!! 次は #grand_final のチャットで待機してください')

#ダブルイリミネーション

        if message.channel.name == 'losers_1_1':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_1 のチャットで待機してください')
        if message.channel.name == 'losers_1_2':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_2 のチャットで待機してください')
        if message.channel.name == 'losers_1_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_3 のチャットで待機してください')
        if message.channel.name == 'losers_1_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_4 のチャットで待機してください')
        if message.channel.name == 'losers_1_5':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_5 のチャットで待機してください')
        if message.channel.name == 'losers_1_6':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_6 のチャットで待機してください')
        if message.channel.name == 'losers_1_7':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_7 のチャットで待機してください')
        if message.channel.name == 'losers_1_8':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_8 のチャットで待機してください')
        if message.channel.name == 'losers_1_9':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_9 のチャットで待機してください')
        if message.channel.name == 'losers_1_10':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_10 のチャットで待機してください')
        if message.channel.name == 'losers_1_11':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_11 のチャットで待機してください')
        if message.channel.name == 'losers_1_12':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_12 のチャットで待機してください')
        if message.channel.name == 'losers_1_13':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_13 のチャットで待機してください')
        if message.channel.name == 'losers_1_14':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_14 のチャットで待機してください')
        if message.channel.name == 'losers_1_15':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_15 のチャットで待機してください')
        if message.channel.name == 'losers_1_16':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_16 のチャットで待機してください')
        if message.channel.name == 'losers_1_17':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_17 のチャットで待機してください')
        if message.channel.name == 'losers_1_18':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_18 のチャットで待機してください')
        if message.channel.name == 'losers_1_19':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_19 のチャットで待機してください')
        if message.channel.name == 'losers_1_20':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_20 のチャットで待機してください')
        if message.channel.name == 'losers_1_21':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_21 のチャットで待機してください')
        if message.channel.name == 'losers_1_22':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_22 のチャットで待機してください')
        if message.channel.name == 'losers_1_23':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_23 のチャットで待機してください')
        if message.channel.name == 'losers_1_24':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_24 のチャットで待機してください')
        if message.channel.name == 'losers_1_25':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_25 のチャットで待機してください')
        if message.channel.name == 'losers_1_26':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_26 のチャットで待機してください')
        if message.channel.name == 'losers_1_27':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_27 のチャットで待機してください')
        if message.channel.name == 'losers_1_28':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_28 のチャットで待機してください')
        if message.channel.name == 'losers_1_29':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_29 のチャットで待機してください')
        if message.channel.name == 'losers_1_30':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_30 のチャットで待機してください')
        if message.channel.name == 'losers_1_31':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_31 のチャットで待機してください')
        if message.channel.name == 'losers_1_32':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_32 のチャットで待機してください')
        if message.channel.name == 'losers_1_33':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_33 のチャットで待機してください')
        if message.channel.name == 'losers_1_34':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_34 のチャットで待機してください')
        if message.channel.name == 'losers_1_35':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_35 のチャットで待機してください')
        if message.channel.name == 'losers_1_36':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_36 のチャットで待機してください')
        if message.channel.name == 'losers_1_37':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_37 のチャットで待機してください')
        if message.channel.name == 'losers_1_38':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_38 のチャットで待機してください')
        if message.channel.name == 'losers_1_39':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_39 のチャットで待機してください')
        if message.channel.name == 'losers_1_40':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_40 のチャットで待機してください')
        if message.channel.name == 'losers_1_41':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_41 のチャットで待機してください')
        if message.channel.name == 'losers_1_42':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_42 のチャットで待機してください')
        if message.channel.name == 'losers_1_42':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_43 のチャットで待機してください')
        if message.channel.name == 'losers_1_44':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_44 のチャットで待機してください')
        if message.channel.name == 'losers_1_45':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_45 のチャットで待機してください')
        if message.channel.name == 'losers_1_46':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_46 のチャットで待機してください')
        if message.channel.name == 'losers_1_47':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_47 のチャットで待機してください')
        if message.channel.name == 'losers_1_48':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_48 のチャットで待機してください')
        if message.channel.name == 'losers_1_49':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_49 のチャットで待機してください')
        if message.channel.name == 'losers_1_50':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_50 のチャットで待機してください')
        if message.channel.name == 'losers_1_51':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_51 のチャットで待機してください')
        if message.channel.name == 'losers_1_52':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_52 のチャットで待機してください')
        if message.channel.name == 'losers_1_53':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_53 のチャットで待機してください')
        if message.channel.name == 'losers_1_54':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_54 のチャットで待機してください')
        if message.channel.name == 'losers_1_55':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_55 のチャットで待機してください')
        if message.channel.name == 'losers_1_56':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_56 のチャットで待機してください')
        if message.channel.name == 'losers_1_57':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_57 のチャットで待機してください')
        if message.channel.name == 'losers_1_58':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_58 のチャットで待機してください')
        if message.channel.name == 'losers_1_59':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_59 のチャットで待機してください')
        if message.channel.name == 'losers_1_60':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_60 のチャットで待機してください')
        if message.channel.name == 'losers_1_61':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_61 のチャットで待機してください')
        if message.channel.name == 'losers_1_62':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_62 のチャットで待機してください')
        if message.channel.name == 'losers_1_63':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_63 のチャットで待機してください')
        if message.channel.name == 'losers_1_64':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_2_64 のチャットで待機してください')
#3回線 losers

        if message.channel.name == 'losers_2_1':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_1 のチャットで待機してください')
        if message.channel.name == 'losers_2_2':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_1 のチャットで待機してください')
        if message.channel.name == 'losers_2_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_2 のチャットで待機してください')
        if message.channel.name == 'losers_2_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_2 のチャットで待機してください')
        if message.channel.name == 'losers_2_5':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_3 のチャットで待機してください')
        if message.channel.name == 'losers_2_6':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_3 のチャットで待機してください')
        if message.channel.name == 'losers_2_7':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_4 のチャットで待機してください')
        if message.channel.name == 'losers_2_8':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_4 のチャットで待機してください')
        if message.channel.name == 'losers_2_9':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_5 のチャットで待機してください')
        if message.channel.name == 'losers_2_10':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_5 のチャットで待機してください')
        if message.channel.name == 'losers_2_11':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_6 のチャットで待機してください')
        if message.channel.name == 'losers_2_12':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_6 のチャットで待機してください')
        if message.channel.name == 'losers_2_13':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_7 のチャットで待機してください')
        if message.channel.name == 'losers_2_14':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_7 のチャットで待機してください')
        if message.channel.name == 'losers_2_15':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_8 のチャットで待機してください')
        if message.channel.name == 'losers_2_16':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_8 のチャットで待機してください')
        if message.channel.name == 'losers_2_17':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_9 のチャットで待機してください')
        if message.channel.name == 'losers_2_18':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_9 のチャットで待機してください')
        if message.channel.name == 'losers_2_19':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_10 のチャットで待機してください')
        if message.channel.name == 'losers_2_20':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_10 のチャットで待機してください')
        if message.channel.name == 'losers_2_21':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_11 のチャットで待機してください')
        if message.channel.name == 'losers_2_22':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_11 のチャットで待機してください')
        if message.channel.name == 'losers_2_23':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_12 のチャットで待機してください')
        if message.channel.name == 'losers_2_24':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_12 のチャットで待機してください')
        if message.channel.name == 'losers_2_25':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_13 のチャットで待機してください')
        if message.channel.name == 'losers_2_26':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_13 のチャットで待機してください')
        if message.channel.name == 'losers_2_27':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_14 のチャットで待機してください')
        if message.channel.name == 'losers_2_28':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_14 のチャットで待機してください')
        if message.channel.name == 'losers_2_29':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_15 のチャットで待機してください')
        if message.channel.name == 'losers_2_30':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_15 のチャットで待機してください')
        if message.channel.name == 'losers_2_31':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_16 のチャットで待機してください')
        if message.channel.name == 'losers_2_32':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_16 のチャットで待機してください')
        if message.channel.name == 'losers_2_33':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_17 のチャットで待機してください')
        if message.channel.name == 'losers_2_34':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_17 のチャットで待機してください')
        if message.channel.name == 'losers_2_35':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_18 のチャットで待機してください')
        if message.channel.name == 'losers_2_36':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_18 のチャットで待機してください')
        if message.channel.name == 'losers_2_37':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_19 のチャットで待機してください')
        if message.channel.name == 'losers_2_38':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_19 のチャットで待機してください')
        if message.channel.name == 'losers_2_39':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_20 のチャットで待機してください')
        if message.channel.name == 'losers_2_40':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_20 のチャットで待機してください')
        if message.channel.name == 'losers_2_41':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_21 のチャットで待機してください')
        if message.channel.name == 'losers_2_42':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_21 のチャットで待機してください')
        if message.channel.name == 'losers_2_43':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_22 のチャットで待機してください')
        if message.channel.name == 'losers_2_44':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_22 のチャットで待機してください')
        if message.channel.name == 'losers_2_45':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_23 のチャットで待機してください')
        if message.channel.name == 'losers_2_46':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_23 のチャットで待機してください')
        if message.channel.name == 'losers_2_47':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_24 のチャットで待機してください')
        if message.channel.name == 'losers_2_48':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_24 のチャットで待機してください')
        if message.channel.name == 'losers_2_49':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_25 のチャットで待機してください')
        if message.channel.name == 'losers_2_50':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_25 のチャットで待機してください')
        if message.channel.name == 'losers_2_51':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_26 のチャットで待機してください')
        if message.channel.name == 'losers_2_52':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_26 のチャットで待機してください')
        if message.channel.name == 'losers_2_53':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_27 のチャットで待機してください')
        if message.channel.name == 'losers_2_54':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_27 のチャットで待機してください')
        if message.channel.name == 'losers_2_55':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_28 のチャットで待機してください')
        if message.channel.name == 'losers_2_56':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_28 のチャットで待機してください')
        if message.channel.name == 'losers_2_57':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_29 のチャットで待機してください')
        if message.channel.name == 'losers_2_58':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_29 のチャットで待機してください')
        if message.channel.name == 'losers_2_59':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_30 のチャットで待機してください')
        if message.channel.name == 'losers_2_60':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_30 のチャットで待機してください')
        if message.channel.name == 'losers_2_61':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_31 のチャットで待機してください')
        if message.channel.name == 'losers_2_62':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_31 のチャットで待機してください')
        if message.channel.name == 'losers_2_63':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_32 のチャットで待機してください')
        if message.channel.name == 'losers_2_64':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_3_32 のチャットで待機してください')
# 4回戦 losers

        if message.channel.name == 'losers_3_1':
            try:
                j = l.index('losers_4_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_1 のチャットで待機してください')
        if message.channel.name == 'losers_3_2':
            try:
                j = l.index('losers_4_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_2 のチャットで待機してください')
        if message.channel.name == 'losers_3_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_3 のチャットで待機してください')
        if message.channel.name == 'losers_3_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_4 のチャットで待機してください')
        if message.channel.name == 'losers_3_5':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_5 のチャットで待機してください')
        if message.channel.name == 'losers_3_6':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_6 のチャットで待機してください')
        if message.channel.name == 'losers_3_7':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_7 のチャットで待機してください')
        if message.channel.name == 'losers_3_8':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_8 のチャットで待機してください')
        if message.channel.name == 'losers_3_9':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_9 のチャットで待機してください')
        if message.channel.name == 'losers_3_10':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_10 のチャットで待機してください')
        if message.channel.name == 'losers_3_11':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_11 のチャットで待機してください')
        if message.channel.name == 'losers_3_12':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_12 のチャットで待機してください')
        if message.channel.name == 'losers_3_13':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_13 のチャットで待機してください')
        if message.channel.name == 'losers_3_14':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_14 のチャットで待機してください')
        if message.channel.name == 'losers_3_15':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_15 のチャットで待機してください')
        if message.channel.name == 'losers_3_16':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_16 のチャットで待機してください')
        if message.channel.name == 'losers_3_17':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_17 のチャットで待機してください')
        if message.channel.name == 'losers_3_18':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_18 のチャットで待機してください')
        if message.channel.name == 'losers_3_19':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_19 のチャットで待機してください')
        if message.channel.name == 'losers_3_20':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_20 のチャットで待機してください')
        if message.channel.name == 'losers_3_21':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_21 のチャットで待機してください')
        if message.channel.name == 'losers_3_22':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_22 のチャットで待機してください')
        if message.channel.name == 'losers_3_23':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_23 のチャットで待機してください')
        if message.channel.name == 'losers_3_24':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_24 のチャットで待機してください')
        if message.channel.name == 'losers_3_25':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_25 のチャットで待機してください')
        if message.channel.name == 'losers_3_26':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_26 のチャットで待機してください')
        if message.channel.name == 'losers_3_27':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_27 のチャットで待機してください')
        if message.channel.name == 'losers_3_28':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_28 のチャットで待機してください')
        if message.channel.name == 'losers_3_29':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_29 のチャットで待機してください')
        if message.channel.name == 'losers_3_30':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_30 のチャットで待機してください')
        if message.channel.name == 'losers_3_31':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_31 のチャットで待機してください')
        if message.channel.name == 'losers_3_32':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_4_32 のチャットで待機してください')

#5回戦 losers

        if message.channel.name == 'losers_4_1':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_5_1 のチャットで待機してください')
        if message.channel.name == 'losers_4_2':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_5_1 のチャットで待機してください')
        if message.channel.name == 'losers_4_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_5_2 のチャットで待機してください')
        if message.channel.name == 'losers_4_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_5_2 のチャットで待機してください')
        if message.channel.name == 'losers_4_5':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_5_3 のチャットで待機してください')
        if message.channel.name == 'losers_4_6':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_5_3 のチャットで待機してください')
        if message.channel.name == 'losers_4_7':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_5_4 のチャットで待機してください')
        if message.channel.name == 'losers_4_8':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_5_4 のチャットで待機してください')
        if message.channel.name == 'losers_4_9':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_5_5 のチャットで待機してください')
        if message.channel.name == 'losers_4_10':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_5_5 のチャットで待機してください')
        if message.channel.name == 'losers_4_11':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_5_6 のチャットで待機してください')
        if message.channel.name == 'losers_4_12':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_5_6 のチャットで待機してください')
        if message.channel.name == 'losers_4_13':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_5_7 のチャットで待機してください')
        if message.channel.name == 'losers_4_14':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_5_7 のチャットで待機してください')
        if message.channel.name == 'losers_4_15':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_5_8 のチャットで待機してください')
        if message.channel.name == 'losers_4_16':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_5_8 のチャットで待機してください')


#6回戦 losers

        if message.channel.name == 'losers_5_1':
            try:
                j = l.index('losers_6_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_6_1 のチャットで待機してください')
        if message.channel.name == 'losers_5_2':
            try:
                j = l.index('losers_6_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_6_2 のチャットで待機してください')

        if message.channel.name == 'losers_5_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_6_3 のチャットで待機してください')
        if message.channel.name == 'losers_5_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_6_4 のチャットで待機してください')
        if message.channel.name == 'losers_5_5':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_6_5 のチャットで待機してください')
        if message.channel.name == 'losers_5_6':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_6_6 のチャットで待機してください')
        if message.channel.name == 'losers_5_7':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_6_7 のチャットで待機してください')
        if message.channel.name == 'losers_5_8':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_6_8 のチャットで待機してください')
#ここから７回戦の誘導 losers
        if message.channel.name == 'losers_6_1':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_7_1 のチャットで待機してください')
        if message.channel.name == 'losers_6_2':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_7_1 のチャットで待機してください')
        if message.channel.name == 'losers_6_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_7_2 のチャットで待機してください')
        if message.channel.name == 'losers_6_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_7_2 のチャットで待機してください')
        if message.channel.name == 'losers_6_5':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_7_3 のチャットで待機してください')
        if message.channel.name == 'losers_6_6':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_7_3 のチャットで待機してください')
        if message.channel.name == 'losers_6_7':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_7_4 のチャットで待機してください')
        if message.channel.name == 'losers_6_8':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_7_4 のチャットで待機してください')

        if message.channel.name == 'losers_7_1':
            try:
                j = l.index('losers_8_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_8_1 のチャットで待機してください')
        if message.channel.name == 'losers_7_2':
            try:
                j = l.index('losers_8_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_8_2 のチャットで待機してください')
        if message.channel.name == 'losers_7_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_8_3 のチャットで待機してください')
        if message.channel.name == 'losers_7_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_8_4 のチャットで待機してください')

        if message.channel.name == 'losers_8_1':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_9_1 のチャットで待機してください')
        if message.channel.name == 'losers_8_2':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_9_1 のチャットで待機してください')
        if message.channel.name == 'losers_8_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_9_3 のチャットで待機してください')
        if message.channel.name == 'losers_8_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_9_4 のチャットで待機してください')

        if message.channel.name == 'losers_9_1':
            try:
                j = l.index('losers_10_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_10_1 のチャットで待機してください')
        if message.channel.name == 'losers_9_2':
            try:
                j = l.index('losers_10_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_10_2 のチャットで待機してください')

        if message.channel.name == 'losers_9_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_10_3 のチャットで待機してください')
        if message.channel.name == 'losers_9_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_10_4 のチャットで待機してください')

        if message.channel.name == 'losers_10_1':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_11_1 のチャットで待機してください')
        if message.channel.name == 'losers_10_2':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_11_1 のチャットで待機してください')
        if message.channel.name == 'losers_10_3':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_11_2 のチャットで待機してください')
        if message.channel.name == 'losers_10_4':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_11_2 のチャットで待機してください')

        if message.channel.name == 'losers_11_1':
            try:
                j = l.index('losers_12_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_12_1 のチャットで待機してください')
        if message.channel.name == 'losers_11_2':
            try:
                j = l.index('losers_12_1')
            except ValueError:
                j = None
            if j == None:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_final のチャットで待機してください')
            else:
                await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_12_2 のチャットで待機してください')

        if message.channel.name == 'losers_12_1':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_13_1 のチャットで待機してください')
        if message.channel.name == 'losers_12_2':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_13_1 のチャットで待機してください')

        if message.channel.name == 'losers_13_1':
            await client.send_message(message.channel, 'おめでとうございます。勝利チームは #losers_final のチャットで待機してください')
#ここからfinal winners
        if message.channel.name == 'losers_final':
            await client.send_message(message.channel, 'Congratulations!!! winners優勝おめでとうございます!! 次は #Grand_final のチャットで待機してください。')
#Grandfinal
        if message.channel.name == 'Grand_final':
            await client.send_message(message.channel, 'Congratulations!!! Grand final 優勝おめでとうございます!! ほんまにおめでとう！')

#ここまで１回戦の誘導
    global miTenko

    if message.content.startswith('!点呼開始'):
        if message.channel.name == '点呼':
            miTenko = ([member.display_name for member in client.get_all_members()])
            bot = client.user.name
            miTenko.remove(bot)
            miTenko.remove('EGM_resultBot')
            await client.send_message(message.channel, '@everyone 点呼を開始しました。メンバーが揃っているチームの代表は、このテキストチャットに　!揃いました　をコピペして送信してください')

    if message.content.startswith('!揃いました'):
        if message.channel.name == '点呼':
            reply = f'{message.author.mention}さんのチームの点呼が完了しました。一回戦のチャットで待機してください'
            await client.send_message(message.channel, reply)
            name = message.author.name
            print(name)
            miTenko.remove(name)
            print(miTenko)
            for i in miTenko:
                user = discord.utils.get(message.server.members, name = i)
                await client.send_message(message.channel, user.mention +'さん！点呼が未完了です')

    if message.content.startswith('!eスポーツルール'):
        reply = '''
        クラス作成制限
以下のアイテムはCWLルールにより使用が制限されています。
        
武器: LMG, ショットガン, 新武器
スコアストリーク: RC-XD, ダート, UAV, ケアパケ, CUAV, セントリー, マンティス
PERK: ドリフター, ガンホー, チームリンク, トラッカー, ゴースト
ワイルドカード: オーバーキル, メインオペレーターMOD, サブオペレーターMOD,
ギア: 音響センサー
アタッチメント; ラピッドファイア, 大口径, 大口径2, レーザーサイト2, マックスロード, ロケットキャッシュ, ハイエクスプロージョン
        
スペシャリスト制限
以下のスペシャリストアイテムはCWLルールにより使用が制限されています。

Ajax: バリスティックシールド, 9
Torque: バリケード, レーザ
Nomad: K9ユニット, メッ
Zero: アイスピック, ディ
Firebreak: リア
Prophet:
Seraph: タッ
Outrider: スパロー, ホーク
        
各使用モードとマップ
        
モード: CWL HARDPOINT
マップ: Arsenal, Frequency, Gridlock, Hacienda, Seaside
モード: CWL SEARCH&DE
マップ: Arsenal, Frequency, Gridlock, Hacienda, Payload
モード: CWL CONTROL
マップ: Arsenal, Frequency. Gridlock, Seaside'''

        await client.send_message(message.channel, reply)
    if message.content.startswith('!GA'):
        reply = '''
        GA制限リスト 更新: 2019/3/25
        
GAを無理強するのは違反行為です。お気をつけください。
        
武器: RAMPART, DMR, SWORDFISH, OUTLOW, SDM, HELLION, C-knife
アタッチメント: ストック2
PERK:
ワイルドカード: オーバーキル, アンダーキル
ギア: アーマー, 装備チャージ
装備: モロトフ, アックス
スペシャリスト: アナイアレーター, センサーダート, グラップルガン(S&Dのみ)
スコアストリーク: ドローン部隊, スナイパーヘリ, スレッシャー, 戦闘ヘリ, ストライクチーム'''

        await client.send_message(message.channel, reply)
    if message.content.startswith('!CES'):
        reply = '準備中'
        await client.send_message(message.channel, reply)

    if message.content.startswith('!BO5 MAP') or message.content.startswith('!bo5'):

        r1 = random.randint(0, len(HPMap)-1)
        r2 = random.randint(0, len(SDMap)-1)
        r3 = random.randint(0, len(CTRMap)-1)
        r4 = random.randint(0, len(HPMap)-1)
        r5 = random.randint(0, len(SDMap)-1)
        HP1 = HPMap[r1]
        SD1 = SDMap[r2]
        CTR = CTRMap[r3]
        HP2 = HPMap[r4]
        SD2 = SDMap[r5]
        reply = '''
        BO5のマップを自動生成しました
        '''
        await client.send_message(message.channel, reply + '\n' + 'HP: ' + HP1 + '\n' + 'S&D: ' + SD1 + '\n' + 'CTR: ' + CTR + '\n' + 'HP: ' + HP2 + '\n' + 'S&D: ' + SD2 + '\n')

    if message.content.startswith('おちんぽ'):
        r = random.uniform(0, 30)
        await client.send_message(message.channel, f'{message.author.mention}さんのおちんぽは' + str(r) + 'cmです')

client.run(str(os.environ.get('BOT_TOKEN')))
