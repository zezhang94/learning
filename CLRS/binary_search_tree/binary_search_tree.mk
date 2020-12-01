##
## Auto Generated makefile by CodeLite IDE
## any manual changes will be erased      
##
## Debug
ProjectName            :=binary_search_tree
ConfigurationName      :=Debug
WorkspaceConfiguration := $(ConfigurationName)
WorkspacePath          :=E:/Projects/CodeLite
ProjectPath            :=E:/Projects/learning/CLRS/binary_search_tree
IntermediateDirectory  :=../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree
OutDir                 :=../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree
CurrentFileName        :=
CurrentFilePath        :=
CurrentFileFullPath    :=
User                   :=yorkz
Date                   :=31/07/2020
CodeLitePath           :=D:/CodeLite
LinkerName             :=C:/MinGW/bin/g++.exe
SharedObjectLinkerName :=C:/MinGW/bin/g++.exe -shared -fPIC
ObjectSuffix           :=.o
DependSuffix           :=.o.d
PreprocessSuffix       :=.i
DebugSwitch            :=-g 
IncludeSwitch          :=-I
LibrarySwitch          :=-l
OutputSwitch           :=-o 
LibraryPathSwitch      :=-L
PreprocessorSwitch     :=-D
SourceSwitch           :=-c 
OutputFile             :=..\..\..\CodeLite\build-$(ConfigurationName)\bin\$(ProjectName)
Preprocessors          :=
ObjectSwitch           :=-o 
ArchiveOutputSwitch    := 
PreprocessOnlySwitch   :=-E
ObjectsFileList        :=$(IntermediateDirectory)/ObjectsList.txt
PCHCompileFlags        :=
RcCmpOptions           := 
RcCompilerName         :=C:/MinGW/bin/windres.exe
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
AR       := C:/MinGW/bin/ar.exe rcu
CXX      := C:/MinGW/bin/g++.exe
CC       := C:/MinGW/bin/gcc.exe
CXXFLAGS :=  -g -O0 -Wall $(Preprocessors)
CFLAGS   :=  -g -O0 -Wall $(Preprocessors)
ASFLAGS  := 
AS       := C:/MinGW/bin/as.exe


##
## User defined environment variables
##
CodeLiteDir:=D:\CodeLite
Objects0=../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/main.c$(ObjectSuffix) ../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/node.c$(ObjectSuffix) ../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/binary_search_tree.c$(ObjectSuffix) 



Objects=$(Objects0) 

##
## Main Build Targets 
##
.PHONY: all clean PreBuild PrePreBuild PostBuild MakeIntermediateDirs
all: MakeIntermediateDirs $(OutputFile)

$(OutputFile): ../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/.d $(Objects) 
	@if not exist "..\..\..\CodeLite\build-$(ConfigurationName)\__\learning\CLRS\binary_search_tree" mkdir "..\..\..\CodeLite\build-$(ConfigurationName)\__\learning\CLRS\binary_search_tree"
	@echo "" > $(IntermediateDirectory)/.d
	@echo $(Objects0)  > $(ObjectsFileList)
	$(LinkerName) $(OutputSwitch)$(OutputFile) @$(ObjectsFileList) $(LibPath) $(Libs) $(LinkOptions)

MakeIntermediateDirs:
	@if not exist "..\..\..\CodeLite\build-$(ConfigurationName)\__\learning\CLRS\binary_search_tree" mkdir "..\..\..\CodeLite\build-$(ConfigurationName)\__\learning\CLRS\binary_search_tree"
	@if not exist ""..\..\..\CodeLite\build-$(ConfigurationName)\bin"" mkdir ""..\..\..\CodeLite\build-$(ConfigurationName)\bin""

../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/.d:
	@if not exist "..\..\..\CodeLite\build-$(ConfigurationName)\__\learning\CLRS\binary_search_tree" mkdir "..\..\..\CodeLite\build-$(ConfigurationName)\__\learning\CLRS\binary_search_tree"

PreBuild:


##
## Objects
##
../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/main.c$(ObjectSuffix): main.c ../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/main.c$(DependSuffix)
	$(CC) $(SourceSwitch) "E:/Projects/learning/CLRS/binary_search_tree/main.c" $(CFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/main.c$(ObjectSuffix) $(IncludePath)
../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/main.c$(DependSuffix): main.c
	@$(CC) $(CFLAGS) $(IncludePath) -MG -MP -MT../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/main.c$(ObjectSuffix) -MF../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/main.c$(DependSuffix) -MM main.c

../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/main.c$(PreprocessSuffix): main.c
	$(CC) $(CFLAGS) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) ../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/main.c$(PreprocessSuffix) main.c

../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/node.c$(ObjectSuffix): node.c ../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/node.c$(DependSuffix)
	$(CC) $(SourceSwitch) "E:/Projects/learning/CLRS/binary_search_tree/node.c" $(CFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/node.c$(ObjectSuffix) $(IncludePath)
../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/node.c$(DependSuffix): node.c
	@$(CC) $(CFLAGS) $(IncludePath) -MG -MP -MT../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/node.c$(ObjectSuffix) -MF../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/node.c$(DependSuffix) -MM node.c

../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/node.c$(PreprocessSuffix): node.c
	$(CC) $(CFLAGS) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) ../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/node.c$(PreprocessSuffix) node.c

../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/binary_search_tree.c$(ObjectSuffix): binary_search_tree.c ../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/binary_search_tree.c$(DependSuffix)
	$(CC) $(SourceSwitch) "E:/Projects/learning/CLRS/binary_search_tree/binary_search_tree.c" $(CFLAGS) $(ObjectSwitch)$(IntermediateDirectory)/binary_search_tree.c$(ObjectSuffix) $(IncludePath)
../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/binary_search_tree.c$(DependSuffix): binary_search_tree.c
	@$(CC) $(CFLAGS) $(IncludePath) -MG -MP -MT../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/binary_search_tree.c$(ObjectSuffix) -MF../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/binary_search_tree.c$(DependSuffix) -MM binary_search_tree.c

../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/binary_search_tree.c$(PreprocessSuffix): binary_search_tree.c
	$(CC) $(CFLAGS) $(IncludePath) $(PreprocessOnlySwitch) $(OutputSwitch) ../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree/binary_search_tree.c$(PreprocessSuffix) binary_search_tree.c


-include ../../../CodeLite/build-$(ConfigurationName)/__/learning/CLRS/binary_search_tree//*$(DependSuffix)
##
## Clean
##
clean:
	$(RM) -r $(IntermediateDirectory)


