##
## Auto Generated makefile by CodeLite IDE
## any manual changes will be erased      
##
## Debug
ProjectName            :=binary_search_tree
ConfigurationName      :=Debug
WorkspaceConfiguration := $(ConfigurationName)
WorkspacePath          :=F:/Projects/CodeLite/simple
ProjectPath            :=F:/Projects/Github/learning/CLRS/binary_search_tree/binary_search_tree
IntermediateDirectory  :=../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree
OutDir                 :=../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree
CurrentFileName        :=
CurrentFilePath        :=
CurrentFileFullPath    :=
User                   :=yorkzhang
Date                   :=27/07/2020
CodeLitePath           :=D:/CodeLite
LinkerName             :=gcc
SharedObjectLinkerName :=gcc -shared -fPIC
ObjectSuffix           :=.o
DependSuffix           :=.o.d
PreprocessSuffix       :=.o.i
DebugSwitch            :=-g 
IncludeSwitch          :=-I
LibrarySwitch          :=-l
OutputSwitch           :=-o 
LibraryPathSwitch      :=-L
PreprocessorSwitch     :=-D
SourceSwitch           :=-c 
OutputFile             :=..\..\..\..\..\CodeLite\simple\build-$(ConfigurationName)\bin\$(ProjectName)
Preprocessors          :=
ObjectSwitch           :=-o 
ArchiveOutputSwitch    := 
PreprocessOnlySwitch   :=-E 
ObjectsFileList        :=$(IntermediateDirectory)/ObjectsList.txt
PCHCompileFlags        :=
RcCmpOptions           := 
RcCompilerName         :=windres
LinkOptions            :=  
IncludePath            :=  $(IncludeSwitch). $(IncludeSwitch). 
IncludePCH             := 
RcIncludePath          := 
Libs                   := 
ArLibs                 :=  
LibPath                := $(LibraryPathSwitch). 

##
## Common variables
## AR, CXX, CC, AS, CXXFLAGS and CFLAGS can be overriden using an environment variables
##
AR       := ar rcus
CXX      := gcc
CC       := gcc
CXXFLAGS :=  -g -O0 -Wall $(Preprocessors)
CFLAGS   :=  -g -O0 -Wall $(Preprocessors)
ASFLAGS  := 
AS       := as


##
## User defined environment variables
##
CodeLiteDir:=D:\CodeLite
Objects0=../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/binary_search_tree.c$(ObjectSuffix) ../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/main.c$(ObjectSuffix) ../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/node.c$(ObjectSuffix) 



Objects=$(Objects0) 

##
## Main Build Targets 
##
.PHONY: all clean PreBuild PrePreBuild PostBuild MakeIntermediateDirs
all: MakeIntermediateDirs $(OutputFile)

$(OutputFile): ../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/.d $(Objects) 
	@if not exist "..\..\..\..\..\CodeLite\simple\build-$(ConfigurationName)\__\__\Github\learning\CLRS\binary_search_tree\binary_search_tree" mkdir "..\..\..\..\..\CodeLite\simple\build-$(ConfigurationName)\__\__\Github\learning\CLRS\binary_search_tree\binary_search_tree"
	@echo "" > $(IntermediateDirectory)/.d
	@echo $(Objects0)  > $(ObjectsFileList)
	$(LinkerName) $(OutputSwitch)$(OutputFile) @$(ObjectsFileList) $(LibPath) $(Libs) $(LinkOptions)

MakeIntermediateDirs:
	@if not exist "..\..\..\..\..\CodeLite\simple\build-$(ConfigurationName)\__\__\Github\learning\CLRS\binary_search_tree\binary_search_tree" mkdir "..\..\..\..\..\CodeLite\simple\build-$(ConfigurationName)\__\__\Github\learning\CLRS\binary_search_tree\binary_search_tree"
	@if not exist ""..\..\..\..\..\CodeLite\simple\build-$(ConfigurationName)\bin"" mkdir ""..\..\..\..\..\CodeLite\simple\build-$(ConfigurationName)\bin""

../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/.d:
	@if not exist "..\..\..\..\..\CodeLite\simple\build-$(ConfigurationName)\__\__\Github\learning\CLRS\binary_search_tree\binary_search_tree" mkdir "..\..\..\..\..\CodeLite\simple\build-$(ConfigurationName)\__\__\Github\learning\CLRS\binary_search_tree\binary_search_tree"

PreBuild:


##
## Objects
##
../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/binary_search_tree.c$(ObjectSuffix): binary_search_tree.c ../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/binary_search_tree.c$(DependSuffix)
	$(CC) $(SourceSwitch) "F:/Projects/Github/learning/CLRS/binary_search_tree/binary_search_tree/binary_search_tree.c" $(CFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/binary_search_tree.c$(ObjectSuffix) $(IncludePath)
../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/binary_search_tree.c$(DependSuffix): binary_search_tree.c
	@$(CC) $(CFLAGS) $(IncludePath) -MG -MP -MT../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/binary_search_tree.c$(ObjectSuffix) -MF../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/binary_search_tree.c$(DependSuffix) -MM binary_search_tree.c

../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/binary_search_tree.c$(PreprocessSuffix): binary_search_tree.c
	$(CC) $(CFLAGS) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) ../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/binary_search_tree.c$(PreprocessSuffix) binary_search_tree.c

../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/main.c$(ObjectSuffix): main.c ../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/main.c$(DependSuffix)
	$(CC) $(SourceSwitch) "F:/Projects/Github/learning/CLRS/binary_search_tree/binary_search_tree/main.c" $(CFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/main.c$(ObjectSuffix) $(IncludePath)
../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/main.c$(DependSuffix): main.c
	@$(CC) $(CFLAGS) $(IncludePath) -MG -MP -MT../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/main.c$(ObjectSuffix) -MF../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/main.c$(DependSuffix) -MM main.c

../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/main.c$(PreprocessSuffix): main.c
	$(CC) $(CFLAGS) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) ../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/main.c$(PreprocessSuffix) main.c

../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/node.c$(ObjectSuffix): node.c ../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/node.c$(DependSuffix)
	$(CC) $(SourceSwitch) "F:/Projects/Github/learning/CLRS/binary_search_tree/binary_search_tree/node.c" $(CFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/node.c$(ObjectSuffix) $(IncludePath)
../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/node.c$(DependSuffix): node.c
	@$(CC) $(CFLAGS) $(IncludePath) -MG -MP -MT../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/node.c$(ObjectSuffix) -MF../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/node.c$(DependSuffix) -MM node.c

../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/node.c$(PreprocessSuffix): node.c
	$(CC) $(CFLAGS) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) ../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree/node.c$(PreprocessSuffix) node.c


-include ../../../../../CodeLite/simple/build-$(ConfigurationName)/__/__/Github/learning/CLRS/binary_search_tree/binary_search_tree//*$(DependSuffix)
##
## Clean
##
clean:
	$(RM) -r $(IntermediateDirectory)


