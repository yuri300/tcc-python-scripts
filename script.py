import os

path = '.'

files = []                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                 
#Analisa pastas e sub-pastas com seus respectivos arquivos .java
for r, d, f in os.walk(path):
    for file in f:
        if '.java' in file:
           files.append(os.path.join(r, file))

#Anotações Framework JUnit
totalTestes                       = 0

totalContTest                     = 0
totalContAfterMethod              = 0
totalContBeforeMethod             = 0
totalContAfter                    = 0
totalContBefore                   = 0
totalContParameterizedTest        = 0
totalContRepeatedTest             = 0
totalContTestFactory              = 0
totalContTestTemplate             = 0
totalContTestMethodOrder          = 0
totalContTestInstance             = 0
totalContDisplayName              = 0
totalContDisplayNameGeneration    = 0
totalContBeforeEach               = 0
totalContAfterEach                = 0
totalContBeforeAll                = 0
totalContAfterAll                 = 0
totalContNested                   = 0
totalContTag                      = 0
totalContDisabled                 = 0
totalContTimeout                  = 0
totalContExtendWith               = 0
totalContRegisterExtension        = 0
totalContTempDir                  = 0

totalContTestOnMac                     = 0
totalContOrder                         = 0
totalContTarget                        = 0
totalContRetention                     = 0
totalContValueSource                   = 0
totalContEnabledOnOs                   = 0
totalContDisabledOnOs                  = 0
totalContEnabledOnJre                  = 0
totalContDisabledOnJre                 = 0
totalContEnabledIfSystemProperty       = 0
totalContDisabledIfSystemProperty      = 0
totalContEnabledIfEnvironmentVariable  = 0
totalContDisabledIfEnvironmentVariable = 0
totalContEnabledIf                     = 0
totalContDisabledIf                    = 0
totalContFast                          = 0
totalContFastTest                      = 0
totalContNullSource                    = 0
totalContEmptySource                   = 0
totalContNullAndEmptySource            = 0
totalContEnumSource                    = 0
totalContMethodSource                  = 0
totalContCsvSource                     = 0
totalContCsvFileSource                 = 0
totalContArgumentsSource               = 0
totalContAggregateWith                 = 0
totalContExecution                     = 0
totalContResourceLock                  = 0
totalContIgnore                        = 0
totalContCategory                      = 0
totalContRunWith                       = 0
totalContRule                          = 0
totalContClassRule                     = 0
totalContEnableRuleMigrationSupport    = 0
totalContEnableJUnit4MigrationSupport  = 0
totalContSuiteDisplayName              = 0
totalContUseTechnicalNames             = 0
totalContSelectPackages                = 0
totalContJvmField                      = 0
totalContInterface                     = 0

contTest                          = 0
contAfterMethod                   = 0
contBeforeMethod                  = 0
contAfter                         = 0
contBefore                        = 0 
contParameterizedTest             = 0
contRepeatedTest                  = 0
contTestFactory                   = 0
contTestTemplate                  = 0
contTestMethodOrder               = 0
contTestInstance                  = 0
contDisplayName                   = 0
contDisplayNameGeneration         = 0
contBeforeEach                    = 0
contAfterEach                     = 0
contBeforeAll                     = 0
contAfterAll                      = 0
contNested                        = 0
contTag                           = 0
contDisabled                      = 0
contTimeout                       = 0
contExtendWith                    = 0
contRegisterExtension             = 0
contTempDir                       = 0

contTestOnMac                     = 0
contOrder                         = 0
contTarget                        = 0
contRetention                     = 0
contValueSource                   = 0
contEnabledOnOs                   = 0
contDisabledOnOs                  = 0
contEnabledOnJre                  = 0
contDisabledOnJre                 = 0
contEnabledIfSystemProperty       = 0
contDisabledIfSystemProperty      = 0
contEnabledIfEnvironmentVariable  = 0
contDisabledIfEnvironmentVariable = 0
contEnabledIf                     = 0
contDisabledIf                    = 0
contFast                          = 0
contFastTest                      = 0
contNullSource                    = 0
contEmptySource                   = 0
contNullAndEmptySource            = 0
contEnumSource                    = 0
contMethodSource                  = 0
contCsvSource                     = 0
contCsvFileSource                 = 0
contArgumentsSource               = 0
contAggregateWith                 = 0
contExecution                     = 0
contResourceLock                  = 0
contIgnore                        = 0
contCategory                      = 0
contRunWith                       = 0
contRule                          = 0
contClassRule                     = 0
contEnableRuleMigrationSupport    = 0
contEnableJUnit4MigrationSupport  = 0
contSuiteDisplayName              = 0
contUseTechnicalNames             = 0
contSelectPackages                = 0
contJvmField                      = 0
contInterface                     = 0

#Contagem de LOCs
incrementaDecrementaTest = 0
LocTest                  = 0
contarComentarioTest     = 0
contarLetrasTest         = 1
achouAbreChaveTest       = None
flagTest                 = None
achouAspasTest           = None
achouTest                = False
achouArrobaTest          = False

incrementaDecrementaAftherMethod = 0
LocAfterMethod                   = 0
achouAbreChaveAfterMethod        = None
flagAfterMethod                  = None
achouAspasAfterMethod            = None
achouAfterMethod                 = False
achouArrobaAfterMethod           = False

incrementaDecrementaBeforeMethod = 0
LocBeforeMethod                  = 0
achouAbreChaveBeforeMethod       = None
flagBeforeMethod                 = None
achouAspasBeforeMethod           = None
achouBeforeMethod                = False
achouArrobaBeforeMethod          = False

incrementaDecrementaAfter = 0
LocAfter                  = 0
contarComentarioAfter     = 0
contarLetrasAfter         = 1 
achouAbreChaveAfter       = None
flagAfter                 = None
achouAspasAfter           = None
achouAfter                = False
achouAspasAfter           = False
achouArrobaAfter          = False

incrementaDecrementaBefore = 0
LocBefore                  = 0
contarComentarioBefore     = 0
contarLetrasBefore         = 1
achouAbreChaveBefore       = None
flagBefore                 = None
achouAspasBefore           = None
achouBefore                = False
achouArrobaBefore          = False

incrementaDecrementaParameterizedTest = 0
LocParameterizedTest                  = 0
achouAbreChaveParameterizedTest       = None
flagParameterizedTest                 = None
achouAspasParameterizedTest           = None
achouParameterizedTest                = False
achouArrobaParameterizedTest          = False

incrementaDecrementaRepeatedTest = 0
LocRepeatedTest                  = 0
achouAbreChaveRepeatedTest       = None
flagRepeatedTest                 = None
achouAspasRepeatTest             = None
achouRepeatedTest                = False
achouArrobaRepeatedTest          = False

incrementaDecrementaTestFactory = 0
LocTestFactory                  = 0
achouAbreChaveTestFactory       = None
flagTestFactory                 = None
achouAspasTestFactory           = None
achouTestFactory                = False
achouArrobaTestFactory          = False

incrementaDecrementaTestTemplate = 0
LocTestTemplate                  = 0
achouAbreChaveTestTemplate       = None
flagTestTemplate                 = None
achouAspasTestTemplate           = None
achouTestTemplate                = False
achouArrobaTestTemplate          = False

incrementaDecrementaTestMethodOrder = 0
LocTestMethodOrder                  = 0
achouAbreChaveTestMethodOrder       = None
flagTestMethodOrder                 = None
achouAspasMethodOrder               = None
achouTestMethodOrder                = False
achouArrobaTestMethodOrder          = False

incrementaDecrementaTestInstance = 0
LocTestInstance                  = 0
achouAbreChaveTestInstance       = None
flagTestInstance                 = None
achouAspasTestInstance           = None
achouTestInstance                = False
achouArrobaTestInstance          = False

incrementaDecrementaDisplayName = 0
LocDisplayName                  = 0
contarComentarioDisplayName     = 0
contarLetrasDisplayName         = 1
achouAbreChaveDisplayName       = None
flagDisplayName                 = None
achouAspasDisplayName           = False
achouDisplayName                = False
achouArrobaDisplayName          = False

incrementaDecrementaDisplayNameGeneration = 0
LocDisplayNameGeneration                  = 0
achouAbreChaveDisplayNameGeneration       = None
flagDisplayNameGeneration                 = None
achouAspasDisplayNameGeneration           = None
achouDisplayNameGeneration                = False
achouArrobaDisplayNameGeneration          = False

incrementaDecrementaBeforeEach = 0
LocBeforeEach                  = 0
achouAbreChaveBeforeEach       = None
flagBeforeEach                 = None
achouAspasBeforeEach           = None
achouBeforeEach                = False
achouArrobaBeforeEach          = False

incrementaDecrementaAfterEach = 0
LocAfterEach                  = 0
achouAbreChaveAfterEach       = None
flagAfterEach                 = None
achouAspasAfterEach           = None
achouAfterEach                = False
achouArrobaAfterEach          = False

incrementaDecrementaBeforeAll = 0
LocBeforeAll                  = 0
achouAbreChaveBeforeAll       = None
flagBeforeAll                 = None
achouAspasBeforeAll           = None
achouBeforeAll                = False
achouArrobaBeforeAll          = False

incrementaDecrementaAfterAll = 0
LocAfterAll                  = 0
achouAbreChaveAfterAll       = None
flagAfterAll                 = None
achouAspasAfterAll           = None
achouAfterAll                = False
achouArrobaAfterAll          = False

incrementaDecrementaNested = 0
LocNested                  = 0
achouAbreChaveNested       = None
flagNested                 = None
achouAspasNested           = None
achouNested                = False
achouArrobaNested          = False

incrementaDecrementaTag = 0
LocTag                  = 0
achouAbreChaveTag       = None
flagTag                 = None
achouAspasTag           = None
achouTag                = False
achouArrobaTag          = False

incrementaDecrementaDisabled = 0
LocDisabled                  = 0
contarComentarioDisabled     = 0
contarLetrasDisabled         = 1
achouAbreChaveDisabled       = None
flagDisabled                 = None
achouAspasDisabled           = None
achouDisabled                = False
achouArrobaDisabled          = False

incrementaDecrementaTimeout = 0
LocTimeout                  = 0
achouAbreChaveTimeout       = None
flagTimeout                 = None
achouAspasTimeout           = None
achouTimeout                = False
achouArrobaTimeout          = False

incrementaDecrementaExtendWith = 0
LocExtendWith                  = 0
achouAbreChaveExtendWith       = None
flagExtendWith                 = None
achouAspasExtendWith           = None
achouExtendWith                = False
achouArrobaExtendWith          = False

incrementaDecrementaRegisterExtension = 0
LocRegisterExtension                  = 0
achouAbreChaveRegisterExtension       = None
flagRegisterExtension                 = None
achouAspasRegisterExtension           = None
achouRegisterExtension                = False
achouArrobaRegisterExtension          = False

incrementaDecrementaTempDir = 0
LocTempDir                  = 0
achouAbreChaveTempDir       = None
flagTempDir                 = None
achouAspasTempDir           = None
achouTempDir                = False
achouArrobaTempDir          = False

incrementaDecrementaTestOnMac = 0
LocTestOnMac                  = 0
achouAbreChaveTestOnMac       = None
flagTestOnMac                 = None
achouAspasTestOnMac           = None
achouTestOnMac                = False
achouArrobaTestOnMac          = False

incrementaDecrementaOrder = 0
LocOrder                  = 0
achouAbreChaveOrder       = None
flagOrder                 = None
achouAspasOrder           = None
achouOrder                = False
achouArrobaOrder          = False

incrementaDecrementaTarget = 0
LocTarget                  = 0
achouAbreChaveTarget       = None
flagTarget                 = None
achouAspasTarget           = None
achouTarget                = False
achouArrobaTarget          = False

incrementaDecrementaRetention = 0
LocRetention                  = 0
achouAbreChaveRetention       = None
flagRetention                 = None
achouAspasRetention           = None
achouRetention                = False
achouArrobaRetention          = False

incrementaDecrementaValueSource = 0
LocValueSource                  = 0
achouAbreChaveValueSource       = None
flagValueSource                 = None
achouAspasValueSource           = None
achouValueSource                = False
achouArrobaValueSource          = False

incrementaDecrementaEnabledOnOs = 0
LocEnabledOnOs                  = 0
achouAbreChaveEnabledOnOs       = None
flagEnabledOnOs                 = None
achouAspasEnabledOnOs           = None
achouEnabledOnOs                = False
achouArrobaEnabledOnOs          = False

incrementaDecrementaDisabledOnOs = 0
LocDisabledOnOs                  = 0
achouAbreChaveDisabledOnOs       = None
flagDisabledOnOs                 = None
achouAspasDisabledOnOs           = None
achouDisabledOnOs                = False
achouArrobaDisabledOnOs          = False

incrementaDecrementaEnabledOnJre = 0
LocEnabledOnJre                  = 0
achouAbreChaveEnabledOnJre       = None
flagEnabledOnJre                 = None
achouAspasEnabledOnJre           = None
achouEnabledOnJre                = False
achouArrobaEnabledOnJre          = False

incrementaDecrementaDisabledOnJre = 0
LocDisabledOnJre                  = 0
achouAbreChaveDisabledOnJre       = None
flagDisabledOnJre                 = None
achouAspasDisabledOnJre           = None
achouDisabledOnJre                = False
achouArrobaDisabledOnJre          = False

incrementaDecrementaEnabledIfSystemProperty = 0
LocEnabledIfSystemProperty                  = 0
achouAbreChaveEnabledIfSystemProperty       = None
flagEnabledIfSystemProperty                 = None
achouAspasEnabledIfSystemProperty           = None
achouEnabledIfSystemProperty                = False
achouArrobaEnabledIfSystemProperty          = False

incrementaDecrementaDisabledIfSystemProperty = 0
LocDisabledIfSystemProperty                  = 0
achouAbreChaveDisabledIfSystemProperty       = None
flagDisabledIfSystemProperty                 = None
achouAspasDisabledIfSystemProperty           = None
achouDisabledIfSystemProperty                = False
achouArrobaDisabledIfSystemProperty          = False

incrementaDecrementaEnabledIfEnvironmentVariable = 0
LocEnabledIfEnvironmentVariable                  = 0
achouAbreChaveEnabledIfEnvironmentVariable       = None
flagEnabledIfEnvironmentVariable                 = None
achouAspasEnabledIfEnvironmentVariable           = None
achouEnabledIfEnvironmentVariable                = False
achouArrobaEnabledIfEnvironmentVariable          = False

incrementaDecrementaDisabledIfEnvironmentVariable = 0
LocDisabledIfEnvironmentVariable                  = 0
achouAbreChaveDisabledIfEnvironmentVariable       = None
flagDisabledIfEnvironmentVariable                 = None
achouAspasDisabledIfEnvironmentVariable           = None
achouDisabledIfEnvironmentVariable                = False
achouDisabledIfEnvironmentVariable                = False

incrementaDecrementaEnabledIf = 0
LocEnabledIf                  = 0
contarComentarioEnabledIf     = 0
contarLetrasEnabledIf         = 1
achouAbreChaveEnabledIf       = None
flagEnabledIf                 = None
achouAspasEnabledIf           = None
achouEnabledIf                = False
achouArrobaEnabledIf          = False

incrementaDecrementaDisabledIf = 0
LocDisabledIf                  = 0
contarComentarioDisabledIf     = 0
contarLetrasDisabledIf         = 1
achouAbreChaveDisabledIf       = None
flagDisabledIf                 = None
achouAspasDisabledIf           = None
achouDisabledIf                = False
achouArrobaDisabledIf          = False

incrementaDecrementaFast = 0
LocFast                  = 0
contarComentarioFast     = 0
contarLetrasFast         = 1 
achouAbreChaveFast       = None
flagFast                 = None
achouAspasFast           = None
achouFast                = False
achouArrobaFast          = False

incrementaDecrementaFastTest = 0
LocFastTest                  = 0
achouAbreChaveFastTest       = None
flagFastTest                 = None
achouAspasFastTest           = None
achouFastTest                = False
achouArrobaFastTest          = False

incrementaDecrementaNullSource = 0
LocNullSource                  = 0
achouAbreChaveNullSource       = None
flagNullSource                 = None
achouAspasNullSource           = None
achouNullSource                = False
achouArrobaNullSource          = False

incrementaDecrementaEmptySource = 0
LocEmptySource                  = 0
achouAbreChaveEmptySource       = None
flagEmptySource                 = None
achouAspasEmptySource           = None
achouEmptySource                = False
achouArrobaEmptySource          = False

incrementaDecrementaNullAndEmptySource = 0
LocNullAndEmptySource                  = 0
achouAbreChaveNullAndEmptySource       = None
flagNullAndEmptySource                 = None
achouAspasNullAndEmptySource           = None
achouNullAndEmptySource                = False
achouArrobaNullAndEmptySource          = False

incrementaDecrementaEnumSource = 0
LocEnumSource                  = 0
achouAbreChaveEnumSource       = None
flagEnumSource                 = None
achouAspasEnumSource           = None
achouEnumSource                = False
achouArrobaEnumSource          = False

incrementaDecrementaMethodSource = 0
LocMethodSource                  = 0
achouAbreChaveMethodSource       = None
flagMethodSource                 = None
achouAspasMethodSource           = None
achouMethodSource                = False
achouArrobaMethodSource          = False

incrementaDecrementaCsvSource = 0
LocCsvSource                  = 0
achouAbreChaveCsvSource       = None
flagCsvSource                 = None
achouAspasCsvSource           = None
achouCsvSource                = False
achouArrobaCsvSource          = False

incrementaDecrementaCsvFileSource = 0
LocCsvFileSource                  = 0
achouAbreChaveCsvFileSource       = None
flagCsvFileSource                 = None
achouAspasCsvFileSource           = None
achouCsvFileSource                = False
achouArrobaCsvFileSource          = False

incrementaDecrementaArgumentsSource = 0
LocArgumentsSource                  = 0
achouAbreChaveArgumentsSource       = None
flagArgumentsSource                 = None
achouAspasArgumentSource            = None
achouArgumentsSource                = False
achouArrobaArgumentsSource          = False

incrementaDecrementaAggregateWith = 0
LocAggregateWith                  = 0
achouAbreChaveAggregateWith       = None
flagAggregateWith                 = None
achouAspasAggregateWith           = None
achouAggregateWith                = False
achouArrobaAggregateWith          = False

incrementaDecrementaExecution = 0
LocExecution                  = 0
achouAbreChaveExecution       = None
flagExecution                 = None
achouAspasExecution           = None
achouExecution                = False
achouArrobaExecution          = False

incrementaDecrementaResourceLock = 0
LocResourceLock                  = 0
achouAbreChaveResourceLock       = None
flagResourceLock                 = None
achouAspasResourceLock           = None
achouResourceLock                = False
achouArrobaResourceLock          = False

incrementaDecrementaIgnore = 0
LocIgnore                  = 0
achouAbreChaveIgnore       = None
flagIgnore                 = None
achouAspasIgnore           = None
achouIgnore                = False
achouArrobaIgnore          = False

incrementaDecrementaCategory = 0
LocCategory                  = 0
achouAbreChaveCategory       = None
flagCategory                 = None
achouAspasCategory           = None
achouCategory                = False
achouArrobaCategory          = False

incrementaDecrementaRunWith = 0
LocRunWith                  = 0
achouAbreChaveRunWith       = None
flagRunWith                 = None
achouAspasRunWith           = None
achouRunWith                = False
achouArrobaRunWith          = False

incrementaDecrementaRule = 0
LocRule                  = 0
achouAbreChaveRule       = None
flagRule                 = None
achouAspasRule           = None
achouRule                = False
achouArrobaRule          = False

incrementaDecrementaClassRule = 0
LocClassRule                  = 0
achouAbreChaveClassRule       = None
flagClassRule                 = None
achouAspasClassRule           = None
achouClassRule                = False
achouArrobaClassRule          = False

incrementaDecrementaEnableRuleMigrationSupport = 0
LocEnableRuleMigrationSupport                  = 0
achouAbreChaveEnableRuleMigrationSupport       = None
flagEnableRuleMigrationSupport                 = None
achouAspasEnableRuleMigrationSupport           = None
achouEnableRuleMigrationSupport                = False
achouArrobaEnableRuleMigrationSupport          = False

incrementaDecrementaEnableJUnit4MigrationSupport = 0
LocEnableJUnit4MigrationSupport                  = 0
achouAbreChaveEnableJUnit4MigrationSupport       = None
flagEnableJUnit4MigrationSupport                 = None
achouAspasEnableJUnit4MigrationSupport           = None
achouEnableJUnit4MigrationSupport                = False
achouArrobaEnableJUnit4MigrationSupport          = False

incrementaDecrementaSuiteDisplayName = 0
LocSuiteDisplayName                  = 0
achouAbreChaveSuiteDisplayName       = None
flagSuiteDisplayName                 = None
achouAspasSuiteDisplayName           = None
achouSuiteDisplayName                = False
achouArrobaSuiteDisplayName          = False

incrementaDecrementaUseTechnicalNames = 0
LocUseTechnicalNames                  = 0
achouAbreChaveUseTechnicalNames       = None
flagUseTechnicalNames                 = None
achouAspasUseTechnicalNames           = None
achouUseTechnicalNames                = False
achouArrobaUseTechnicalNames          = False

incrementaDecrementaSelectPackages = 0
LocSelectPackages                  = 0
achouAbreChaveSelectPackages       = None
flagSelectPackages                 = None
achouAspasSelectPackages           = None
achouSelectPackages                = False
achouArrobaSelectPackages          = False

incrementaDecrementaJvmField = 0
LocJvmField                  = 0
achouAbreChaveJvmField       = None
flagJvmField                 = None
achouAspasJvmField           = None
achouJvmField                = False
achouArrobaJvmField          = False

incrementaDecrementaInterface = 0
LocInterface                  = 0
achouAbreChaveInterface       = None
flagInterface                 = None
achouAspasInterface           = None
achouInterface                = False
achouArrobaInterface          = False

barraPraComentarioTest                  = False
barraPraComentarioAfter                 = False
barraPraComentarioBefore                = False
barraPraComentarioAfterMethod           = False
barraPraComentarioBeforeMethod          = False
barraPraComentarioParameterizedTest     = False
barraPraComentarioRepeatedTest          = False
barraPraComentarioTestFactory           = False
barraPraComentarioTestTemplate          = False
barraPraComentarioTestMethodOrder       = False
barraPraComentarioTestInstance          = False
barraPraComentarioDisplayName           = False
barraPraComentarioDisplayNameGeneration = False
barraPraComentarioBeforeEach            = False
barraPraComentarioAfterEach             = False
barraPraComentarioBeforeAll             = False
barraPraComentarioAfterAll              = False
barraPraComentarioNested                = False
barraPraComentarioTag                   = False
barraPraComentarioDisabled              = False
barraPraComentarioTimeout               = False
barraPraComentarioExtendWith            = False
barraPraComentarioRegisterExtension     = False
barraPraComentarioTempDir               = False

barraPraComentarioTestOnMac                     = False
barraPraComentarioOrder                         = False
barraPraComentarioTarget                        = False
barraPraComentarioRetention                     = False
barraPraComentarioValueSource                   = False
barraPraComentarioEnabledOnOs                   = False
barraPraComentarioDisabledOnOs                  = False
barraPraComentarioEnabledOnJre                  = False
barraPraComentarioDisabledOnJre                 = False
barraPraComentarioEnabledIfSystemProperty       = False
barraPraComentarioDisabledIfSystemProperty      = False
barraPraComentarioEnabledIfEnvironmentVariable  = False
barraPraComentarioDisabledIfEnvironmentVariable = False
barraPraComentarioEnabledIf                     = False
barraPraComentarioDisabledIf                    = False
barraPraComentarioFast                          = False
barraPraComentarioFastTest                      = False
barraPraComentarioNullSource                    = False
barraPraComentarioEmptySource                   = False
barraPraComentarioNullAndEmptySource            = False
barraPraComentarioEnumSource                    = False
barraPraComentarioMethodSource                  = False
barraPraComentarioCsvSource                     = False
barraPraComentarioCsvFileSource                 = False
barraPraComentarioArgumentsSource               = False
barraPraComentarioAggregateWith                 = False
barraPraComentarioExecution                     = False
barraPraComentarioResourceLock                  = False
barraPraComentarioIgnore                        = False
barraPraComentarioCategory                      = False
barraPraComentarioRunWith                       = False
barraPraComentarioRule                          = False
barraPraComentarioClassRule                     = False
barraPraComentarioEnableRuleMigrationSupport    = False
barraPraComentarioEnableJUnit4MigrationSupport  = False
barraPraComentarioSuiteDisplayName              = False
barraPraComentarioUseTechnicalNames             = False
barraPraComentarioSelectPackages                = False
barraPraComentarioJvmField                      = False
barraPraComentarioInterface                     = False

#Anotações Framework TestNG
barraPraComentarioAfterSuite   = False
barraPraComentarioAfterClass   = False
barraPraComentarioAfterTest    = False
barraPraComentarioAfterGroups  = False

barraPraComentarioBeforeSuite  = False
barraPraComentarioBeforeClass  = False
barraPraComentarioBeforeTest   = False
barraPraComentarioBeforeGroups = False

#Arquivo .java encontrado, analisa a quantidade de testes realizados ao mesmo
for f in files:

   datafile = open(f, errors="ignore")                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                         
   for line in datafile:
       if '@Test' in line:
           tamanho = (len(line) - 1)
           #Verifica se a linha da assinatura e um comentario
           for letra in line:
               if (letra == "/"):
                   barraPraComentarioTest = True
               elif (letra == '"'):
                     achouAspasTest = True
               elif (letra == "@"):
                     flagAfterMethod        = True
                     achouArrobaAfterMethod = True
                     break
               
           if '@TestFactory' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioTestFactory = True
                   elif (letra == "@"):
                         break
                         
           if '@TestTemplate' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioTestTemplate = True
                   elif (letra == "@"):
                         break
                         
           if '@TestMethodOrder' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioTestMethodOrder = True
                   elif (letra == "@"):
                         break
                         
           if '@TestInstance' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioTestInstance = True
                   elif (letra == "@"):
                         break
           
           if '@TestOnMac' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioTestOnMac = True
                   elif (letra == "@"):
                         break
                         
           #So entra na condicao se a assinatura for um comentario
           if ((barraPraComentarioTest != barraPraComentarioTestFactory)     and
              (barraPraComentarioTest  != barraPraComentarioTestTemplate)    and
              (barraPraComentarioTest  != barraPraComentarioTestMethodOrder) and
              (barraPraComentarioTest  != barraPraComentarioTestInstance)    and
              (barraPraComentarioTest  != barraPraComentarioTestOnMac)):
               for letra in line:
                   if (letra == "/"):
                       contarComentarioTest += 1
                   elif (letra == " ") or (letra == "	"):
                         contarComentarioTest += 1
                   else:
                       if (contarLetrasTest <= 5):
                           contarLetrasTest += 1
                       else:
                           contarComentarioTest += 1
                           
           #So entra na condicao  com a comparacao e validacao das mesmas assinaturas @Test
           if (len("@Test") != (tamanho - (contarComentarioTest - 1)) and (barraPraComentarioTest == False) and (achouAspasTest == False)):
               #A assinatura nao sendo comentario sai verificando o que vem depois do mesmo
               for letra in line:
                   if ((letra == " ")or(letra == "	")):
                       contarAssinaturaTest += 1
                   elif (letra == "/"):
                         contarAssinaturaTest += 1
        
               for letra in line:
                   if (letra == "/"):
                       achouBarraTest = True
                   elif (achouBarraTest == True):
                         if ((letra != " ")and(letra != "	")):
                             contarAssinaturaTest += 1
                             decrementaTest       = True
                                       
               if (decrementaTest == True):
                   if (len("@Test") == (tamanho - (contarAssinaturaTest - 1))):                 
                       achouAbreChaveTest = False
                       achouTest          = True  
                       contTest           += 1
               else:
                   if (len("@Test") == (tamanho - contarAssinaturaTest)):
                       achouAbreChaveTest = False
                       achouTest          = True  
                       contTest           += 1

               if (achouTest != True):
                   contarLetrasTest   = 0
                   contarAspas        = 0
                   naoEhTest          = None
                   concatenarPalavras = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagTest == True) and (achouArrobaTest == True)):
                               if (letra == "@"):
                                   if ((naoEhTest == True) and (contarLetrasTest == 5)):
                                       if ('@Test' == concatenarPalavras):
                                           achouAbreChaveTest = False
                                           achouTest          = True
                                           naoEhTest          = False
                                           contTest           += 1
                                           contarLetrasTest   = 1
                                           concatenarPalavras = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasTest   = 1
                                       achouArrobaTest    = True
                                       concatenarPalavras = ""
                                   
                                   contarLetrasTest   = 1
                                   concatenarPalavras += letra
                                   
                               elif (achouArrobaTest == True):
                                     if (contarLetrasTest == 5):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@Test' == concatenarPalavras):
                                                 achouAbreChaveTest = False
                                                 achouTest          = True
                                                 naoEhTest          = False
                                                 contTest           += 1
                                                 contarLetrasTest   = 0
                                                 concatenarPalavras = ""
                                             if (letra == "("):
                                                 concatenarPalavras = ""
                                                 flagTest           = False
                                                 achouArrobaTest    = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasTest += 1
                                             naoEhTest        = False
                                             
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras = ""
                                             flagTest           = False
                                             achouArrobaTest    = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasTest = 0
                                             
                                             if ((letra != " ")and(letra != "   ")):                                             
                                                 concatenarPalavras += letra
                                             
                                             contarLetrasTest += 1
                                             naoEhTest        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasTest = True
                                   contarAspas    += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas    -= 2
                                   achouAspasTest = False
                                   
                               if (achouAspasTest != True):
                                   if (letra == ")"):
                                       flagTest        = True 
                                       achouArrobaTest = True
                                   elif (letra == "@"):
                                         concatenarPalavras = ""
                                         concatenarPalavras += letra
                                         contarLetrasTest   = 1
                                         flagTest           = True
                                         achouArrobaTest    = True
                                     
                       else:
                           if ((naoEhTest == True) and (contarLetrasTest == 5)):
                               if ('@Test' == concatenarPalavras):
                                   concatenarPalavras     = ""
                                   achouAbreChaveTest     = False
                                   achouTest              = True
                                   naoEhTest              = False
                                   contTest               += 1
                                   contarLetrasTest       = 0
                                   barraPraComentarioTest = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @Test
                   if (barraPraComentarioTest != True):
                       if ((len("@Test") == contarLetrasTest) or (len("@Test") == contarLetrasTest - 1)):
                           if ('@Test' == concatenarPalavras):
                               concatenarPalavras = ""
                               contarLetrasTest   = 0
                               achouAbreChaveTest = False
                               achouTest          = True
                               contTest           += 1
                   
       #Inicializando os valores
       contarAssinaturaTest = 0
       achouBarraTest       = False
       achouArrobaTest      = False
       achouAspasTest       = False
       decrementaTest       = False
       
       achouTest = False
       
       contarComentarioTest = 0
       contarLetrasTest     = 1        
       barraPraComentarioTest            = False
       barraPraComentarioTestFactory     = False
       barraPraComentarioTestTemplate    = False
       barraPraComentarioTestMethodOrder = False
       barraPraComentarioTestInstance    = False
       barraPraComentarioTestOnMac       = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@AfterMethod' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioAfterMethod = True
               elif (letra == '"'):
                     achouAspasAfterMethod = True
               elif (letra == "@"):
                     flagAfterMethod        = True
                     achouArrobaAfterMethod = True
                     break
 
           if (barraPraComentarioAfterMethod != True):
               if (achouAspasAfterMethod != True):
                   contarLetrasAfterMethod = 0
                   contarAspas             = 0
                   naoEhAfterMethod        = None
                   concatenarPalavras      = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagAfterMethod == True) and (achouArrobaAfterMethod == True)):
                               if (letra == "@"):
                                   if ((naoEhAfterMethod == True) and (contarLetrasAfterMethod == 12)):
                                       if ('@AfterMethod' == concatenarPalavras):
                                           achouAbreChaveAfterMethod = False
                                           achouAfterMethod          = True
                                           naoEhAfterMethod          = False
                                           contAfterMethod           += 1
                                           contarLetrasAfterMethod   = 1
                                           concatenarPalavras        = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasAfterMethod = 1
                                       achouArrobaAfterMethod  = True
                                       concatenarPalavras      = ""
                                   
                                   contarLetrasAfterMethod = 1
                                   concatenarPalavras      += letra
                                   
                               elif (achouArrobaAfterMethod == True):
                                     if (contarLetrasAfterMethod == 12):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@AfterMethod' == concatenarPalavras):
                                                 achouAbreChaveAfterMethod = False
                                                 achouAfterMethod          = True
                                                 naoEhAfterMethod          = False
                                                 contAfterMethod           += 1
                                                 contarLetrasAfterMethod   = 0
                                                 concatenarPalavras        = ""
                                             if (letra == "("):
                                                 concatenarPalavras     = ""
                                                 flagAfterMethod        = False
                                                 achouArrobaAfterMethod = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasAfterMethod += 1
                                             naoEhAfterMethod        = False
                                             
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras     = ""
                                             flagAfterMethod        = False
                                             achouArrobaAfterMethod = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasAfterMethod = 0
                                             
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                             
                                             contarLetrasAfterMethod += 1
                                             naoEhAfterMethod        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasAfterMethod = True
                                   contarAspas           += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas -= 2
                                   achouAspasAfterMethod = False
                                   
                               if (achouAspasAfterMethod != True):
                                   if (letra == ")"):
                                       flagAfterMethod        = True 
                                       achouArrobaAfterMethod = True
                                   elif (letra == "@"):
                                         concatenarPalavras      = ""
                                         concatenarPalavras      += letra
                                         contarLetrasAfterMethod = 1
                                         flagAfterMethod         = True
                                         achouArrobaAfterMethod  = True
                                     
                       else:
                           if ((naoEhAfterMethod == True) and (contarLetrasAfterMethod == 12)):
                               if ('@AfterMethod' == concatenarPalavras):
                                   concatenarPalavras            = ""
                                   achouAbreChaveAfterMethod     = False
                                   achouAfterMethod              = True
                                   naoEhAfterMethod              = False
                                   contAfterMethod               += 1
                                   contarLetrasAfterMethod       = 0
                                   barraPraComentarioAfterMethod = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @AfterMethod
                   if (barraPraComentarioAfterMethod != True):
                       if ((len("@AfterMethod") == contarLetrasAfterMethod) or (len("@AfterMethod") == contarLetrasAfterMethod - 1)):
                           if ('@AfterMethod' == concatenarPalavras):
                               concatenarPalavras        = ""
                               contarLetrasAfterMethod   = 0
                               achouAbreChaveAfterMethod = False
                               achouAfterMethod          = True
                               contAfterMethod           += 1
             
       achouArrobaAfterMethod        = False
       achouAspasAfterMethod         = False
       barraPraComentarioAfterMethod = False
       
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@BeforeMethod' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioBeforeMethod = True
               elif (letra == '"'):
                     achouAspasBeforeMethod = True
               elif (letra == "@"):
                     flagBeforeMethod        = True
                     achouArrobaBeforeMethod = True
                     break
           
           if (barraPraComentarioBeforeMethod != True):
               if (achouAspasBeforeMethod != True):
                   contarLetrasBeforeMethod = 0
                   contarAspas              = 0
                   naoEhBeforeMethod        = None
                   concatenarPalavras       = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagBeforeMethod == True) and (achouArrobaBeforeMethod == True)):
                               if (letra == "@"):
                                   if ((naoEhBeforeMethod == True) and (contarLetrasBeforeMethod == 13)):
                                       if ('@BeforeMethod' == concatenarPalavras):
                                           achouAbreChaveBeforeMethod = False
                                           achouBeforeMethod          = True
                                           naoEhBeforeMethod          = False
                                           contBeforeMethod           += 1
                                           contarLetrasBeforeMethod   = 1
                                           concatenarPalavras         = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasBeforeMethod = 1
                                       achouArrobaBeforeMethod  = True
                                       concatenarPalavras       = ""
                                       
                                   contarLetrasBeforeMethod = 1
                                   concatenarPalavras       += letra
                                   
                               elif (achouArrobaBeforeMethod == True):
                                     if (contarLetrasBeforeMethod == 13):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@BeforeMethod' == concatenarPalavras):
                                                 achouAbreChaveBeforeMethod = False
                                                 achouBeforeMethod          = True
                                                 naoEhBeforeMethod          = False
                                                 contBeforeMethod           += 1
                                                 contarLetrasBeforeMethod   = 0
                                                 concatenarPalavras = ""
                                             if (letra == "("):
                                                 concatenarPalavras      = ""
                                                 flagBeforeMethod        = False
                                                 achouArrobaBeforeMethod = False
                                                 
                                         else:
                                             if ((letra != " ")or(letra != " ")):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasBeforeMethod += 1
                                             naoEhBeforeMethod        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras      = ""
                                             flagBeforeMethod        = False
                                             achouArrobaBeforeMethod = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasBeforeMethod = 0
                                             
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasBeforeMethod += 1
                                             naoEhBeforeMethod        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasBeforeMethod = True
                                   contarAspas            += 1
                               
                               if (contarAspas == 2):
                                   contarAspas            -= 2
                                   achouAspasBeforeMethod = False
                                   
                               if (achouAspasBeforeMethod != True):
                                   if (letra == ")"):
                                       flagBeforeMethod        = True 
                                       achouArrobaBeforeMethod = True
                                   elif (letra == "@"):
                                         concatenarPalavras       = ""
                                         concatenarPalavras       += letra
                                         contarLetrasBeforeMethod = 1
                                         flagBeforeMethod         = True
                                         achouArrobaBeforeMethod  = True
                                     
                       else:
                           if ((naoEhBeforeMethod == True) and (contarLetrasBeforeMethod == 13)):
                               if ('@BeforeMethod' == concatenarPalavras):
                                   concatenarPalavras             = ""
                                   achouAbreChaveBeforeMethod     = False
                                   achouBeforeMethod              = True
                                   naoEhBeforeMethod              = False
                                   contBeforeMethod               += 1
                                   contarLetrasBeforeMethod       = 0
                                   barraPraComentarioBeforeMethod = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @BeforeMethod
                   if (barraPraComentarioBeforeMethod != True):
                       if ((len("@BeforeMethod") == contarLetrasBeforeMethod) or (len("@BeforeMethod") == contarLetrasBeforeMethod - 1)):
                           if ('@BeforeMethod' == concatenarPalavras):
                               concatenarPalavras         = ""
                               contarLetrasBeforeMethod   = 0
                               achouAbreChaveBeforeMethod = False
                               achouBeforeMethod          = True
                               contBeforeMethod           += 1
             
       achouArrobaBeforeMethod        = False
       achouAspasBeforeMethod         = False
       barraPraComentarioBeforeMethod = False 
   
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@After' in line:
           tamanho = (len(line) - 1)
           #Verifica se a linha da assinatura e um comentario
           for letra in line:
               if (letra == "/"):
                   barraPraComentarioAfter = True
               elif (letra == '"'):
                     achouAspasAfter = True
               elif (letra == "@"):
                     break
                     
           if '@AfterMethod' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioAfterMethod = True
                   elif (letra == "@"):
                         break
                         
           if '@AfterEach' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioAfterEach = True
                   elif (letra == "@"):
                         break
                         
           if '@AfterAll' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioAfterAll = True
                   elif (letra == "@"):
                         break
                         
           if '@AfterSuite' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioAfterSuite = True
                   elif (letra == "@"):
                         break
           
           if '@AfterClass' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioAfterClass = True
                   elif (letra == "@"):
                         break
                         
           if '@AfterTest' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioAfterTest = True
                   elif (letra == "@"):
                         break
                         
           if '@AfterGroups' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioAfterGroups = True
                   elif (letra == "@"):
                         break
                         
           #So entra na condicao se a assinatura for um comentario
           if ((barraPraComentarioAfter != barraPraComentarioAfterMethod) and
              (barraPraComentarioAfter  != barraPraComentarioAfterEach)   and
              (barraPraComentarioAfter  != barraPraComentarioAfterAll)    and
              (barraPraComentarioAfter  != barraPraComentarioAfterSuite)  and
              (barraPraComentarioAfter  != barraPraComentarioAfterClass)  and
              (barraPraComentarioAfter  != barraPraComentarioAfterTest)   and
              (barraPraComentarioAfter  != barraPraComentarioAfterGroups)):
               for letra in line:
                   if (letra == "/"):
                       contarComentarioAfter += 1
                   elif (letra == " ") or (letra == "	"):
                         contarComentarioAfter += 1
                   else:
                       if (contarLetrasAfter <= 6):
                           contarLetrasAfter += 1
                       else:
                           contarComentarioAfter += 1
         
           #So entra na condicao  com a comparacao e validacao das mesmas assinaturas @After
           if (len("@After") != (tamanho - (contarComentarioAfter - 1)) and (barraPraComentarioAfter == False) and (achouAspasAfter == False)):
               #A assinatura nao sendo comentario sai verificando o que vem depois do mesmo
               for letra in line:
                   if ((letra == " ")or(letra == "	")):
                       contarAssinaturaAfter += 1
                   elif (letra == "/"):
                         contarAssinaturaAfter += 1
        
               for letra in line:
                   if (letra == "/"):
                       achouBarraAfter = True
                   elif (achouBarraAfter == True):
                         if ((letra != " ")and(letra != "	")):
                             contarAssinaturaAfter += 1
                             decrementaAfter       = True
                             
               if (decrementaAfter == True):
                   if (len("@After") == (tamanho - (contarAssinaturaAfter - 1))):                 
                       achouAbreChaveAfter = False
                       achouAfter          = True  
                       contAfter           += 1
               else:
                   if (len("@After") == (tamanho - contarAssinaturaAfter)):
                       achouAbreChaveAfter = False
                       achouAfter          = True  
                       contAfter           += 1

               if (achouAfter != True):
                   contarLetrasAfter = 0
                   contarAspas       = 0
                   naoEhAfter        = None
                   concatenarPalavras = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagAfter == True) and (achouArrobaAfter == True)):
                               if (letra == "@"):
                                   if ((naoEhAfter == True) and (contarLetrasAfter == 6)):
                                       if ('@After' == concatenarPalavras):
                                           achouAbreChaveAfter = False
                                           achouAfter          = True
                                           naoEhAfter          = False
                                           contAfter           += 1
                                           contarLetrasAfter   = 1
                                           concatenarPalavras  = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasAfter  = 1
                                       achouArrobaAfter   = True
                                       concatenarPalavras = ""
                                   
                                   contarLetrasAfter  = 1
                                   concatenarPalavras += letra
                                   
                               elif (achouArrobaAfter == True):
                                     if (contarLetrasAfter == 6):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@After' == concatenarPalavras):
                                                 achouAbreChaveAfter = False
                                                 achouAfter          = True
                                                 naoEhAfter          = False
                                                 contAfter           += 1
                                                 contarLetrasAfter   = 0
                                                 concatenarPalavras  = ""
                                             if (letra == "("):
                                                 concatenarPalavras  = ""
                                                 flagAfter           = False
                                                 achouArrobaAfter    = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasAfter += 1
                                             naoEhAfter        = False
                                             
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras  = ""
                                             flagAfter           = False
                                             achouArrobaAfter    = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasAfter = 0
                                             
                                             if ((letra != " ")and(letra != "   ")):                                             
                                                 concatenarPalavras += letra
                                             
                                             contarLetrasAfter += 1
                                             naoEhAfter        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasAfter = True
                                   contarAspas     += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas     -= 2
                                   achouAspasAfter = False
                                   
                               if (achouAspasAfter != True):
                                   if (letra == ")"):
                                       flagAfter        = True 
                                       achouArrobaAfter = True
                                   elif (letra == "@"):
                                         concatenarPalavras  = ""
                                         concatenarPalavras  += letra
                                         contarLetrasAfter   = 1
                                         flagAfter           = True
                                         achouArrobaAfter    = True
                                     
                       else:
                           if ((naoEhAfter == True) and (contarLetrasAfter == 6)):
                               if ('@After' == concatenarPalavras):
                                   concatenarPalavras      = ""
                                   achouAbreChaveAfter     = False
                                   achouAfter              = True
                                   naoEhAfter              = False
                                   contAfter               += 1
                                   contarLetrasAfter       = 0
                                   barraPraComentarioAfter = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @After
                   if (barraPraComentarioAfter != True):
                       if ((len("@After") == contarLetrasAfter) or (len("@After") == contarLetrasAfter - 1)):
                           if ('@After' == concatenarPalavras):
                               concatenarPalavras  = ""
                               contarLetrasAfter   = 0
                               achouAbreChaveAfter = False
                               achouAfter          = True
                               contAfter           += 1
       
       #Inicializando os valores
       contarAssinaturaAfter = 0
       achouBarraAfter       = False
       achouArrobaAfter      = False
       achouAspasAfter       = False
       decrementaAfter       = False
       
       achouAfter = False
       
       contarComentarioAfter  = 0
       contarLetrasAfter      = 1 
       barraPraComentarioAfter       = False
       barraPraComentarioAfterMethod = False
       barraPraComentarioAfterEach   = False
       barraPraComentarioAfterAll    = False
       
       barraPraComentarioAfterSuite  = False
       barraPraComentarioAfterClass  = False
       barraPraComentarioAfterTest   = False
       barraPraComentarioAfterGroups = False

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@Before' in line:
           tamanho = (len(line) - 1)
           #Verifica se a linha da assinatura e um comentario
           for letra in line:
               if (letra == "/"):
                   barraPraComentarioBefore = True
               elif (letra == '"'):
                     achouAspasBefore = True
               elif (letra == "@"):
                     break
                     
           if '@BeforeMethod' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioBeforeMethod = True
                   elif (letra == "@"):
                         break
                         
           if '@BeforeEach' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioBeforeEach = True
                   elif (letra == "@"):
                         break
                         
           if '@BeforeAll' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioBeforeAll = True
                   elif (letra == "@"):
                         break
                         
           if '@BeforeSuite' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioBeforeSuite = True
                   elif (letra == "@"):
                         break
           
           if '@BeforeTest' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioBeforeTest = True
                   elif (letra == "@"):
                         break
                         
           if '@BeforeClass' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioBeforeClass = True
                   elif (letra == "@"):
                         break
           
           if '@BeforeGroups' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioBeforeGroups = True
                   elif (letra == "@"):
                         break
                         
           #So entra na condicao se a assinatura for um comentario
           if ((barraPraComentarioBefore != barraPraComentarioBeforeMethod) and
              (barraPraComentarioBefore  != barraPraComentarioBeforeEach)   and
              (barraPraComentarioBefore  != barraPraComentarioBeforeAll)    and
              (barraPraComentarioBefore  != barraPraComentarioBeforeSuite)  and
              (barraPraComentarioBefore  != barraPraComentarioBeforeTest)   and
              (barraPraComentarioBefore  != barraPraComentarioBeforeClass)  and
              (barraPraComentarioBefore  != barraPraComentarioBeforeGroups)):
               for letra in line:
                   if (letra == "/"):
                       contarComentarioBefore += 1
                   elif (letra == " ") or (letra == "	"):
                         contarComentarioBefore += 1
                   else:
                       if (contarLetrasBefore <= 7):
                           contarLetrasBefore += 1
                       else:
                           contarComentarioBefore += 1
         
           #So entra na condicao  com a comparacao e validacao das mesmas assinaturas @Before
           if (len("@Before") != (tamanho - (contarComentarioBefore - 1)) and (barraPraComentarioBefore == False) and (achouAspasBefore == False)):
               #A assinatura nao sendo comentario sai verificando o que vem depois do mesmo
               for letra in line:
                   if ((letra == " ")or(letra == "	")):
                       contarAssinaturaBefore += 1
                   elif (letra == "/"):
                         contarAssinaturaBefore += 1
        
               for letra in line:
                   if (letra == "/"):
                       achouBarraBefore = True
                   elif (achouBarraBefore == True):
                         if ((letra != " ")and(letra != "	")):
                             contarAssinaturaBefore += 1
                             decrementaBefore       = True
                             
               if (decrementaBefore == True):
                   if (len("@Before") == (tamanho - (contarAssinaturaBefore - 1))):                 
                       achouAbreChaveBefore = False
                       achouBefore          = True  
                       contBefore           += 1
               else:
                   if (len("@Before") == (tamanho - contarAssinaturaBefore)):
                       achouAbreChaveBefore = False
                       achouBefore          = True  
                       contBefore           += 1

               if (achouBefore != True):
                   contarLetrasBefore = 0
                   contarAspas        = 0
                   naoEhBefore        = None
                   concatenarPalavras = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagBefore == True) and (achouArrobaBefore == True)):
                               if (letra == "@"):
                                   if ((naoEhBefore == True) and (contarLetrasBefore == 7)):
                                       if ('@Before' == concatenarPalavras):
                                           achouAbreChaveBefore = False
                                           achouBefore          = True
                                           naoEhBefore          = False
                                           contBefore           += 1
                                           contarLetrasBefore   = 1
                                           concatenarPalavras   = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasBefore = 1
                                       achouArrobaBefore  = True
                                       concatenarPalavras = ""
                                   
                                   contarLetrasBefore = 1
                                   concatenarPalavras += letra
                                   
                               elif (achouArrobaBefore == True):
                                     if (contarLetrasBefore == 7):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@Before' == concatenarPalavras):
                                                 achouAbreChaveBefore = False
                                                 achouBefore          = True
                                                 naoEhBefore          = False
                                                 contBefore           += 1
                                                 contarLetrasBefore   = 0
                                                 concatenarPalavras   = ""
                                             if (letra == "("):
                                                 concatenarPalavras = ""
                                                 flagBefore         = False
                                                 achouArrobaBefore  = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasBefore += 1
                                             naoEhBefore        = False
                                             
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras   = ""
                                             flagBefore           = False
                                             achouArrobaBefore    = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasBefore = 0
                                             
                                             if ((letra != " ")and(letra != "   ")):                                             
                                                 concatenarPalavras += letra
                                             
                                             contarLetrasBefore += 1
                                             naoEhBefore        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasBefore = True
                                   contarAspas      += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas      -= 2
                                   achouAspasBefore = False
                                   
                               if (achouAspasBefore != True):
                                   if (letra == ")"):
                                       flagTest          = True 
                                       achouArrobaBefore = True
                                   elif (letra == "@"):
                                         concatenarPalavras   = ""
                                         concatenarPalavras   += letra
                                         contarLetrasBefore   = 1
                                         flagBefore           = True
                                         achouArrobaBefore    = True
                                     
                       else:
                           if ((naoEhBefore == True) and (contarLetrasBefore == 7)):
                               if ('@Before' == concatenarPalavras):
                                   concatenarPalavras       = ""
                                   achouAbreChaveBefore     = False
                                   achouBefore              = True
                                   naoEhBefore              = False
                                   contBefore               += 1
                                   contarLetrasBefore       = 0
                                   barraPraComentarioBefore = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @Before
                   if (barraPraComentarioBefore != True):
                       if ((len("@Before") == contarLetrasBefore) or (len("@Before") == contarLetrasBefore - 1)):
                           if ('@Before' == concatenarPalavras):
                               concatenarPalavras   = ""
                               contarLetrasBefore   = 0
                               achouAbreChaveBefore = False
                               achouBefore          = True
                               contBefore           += 1
       
       #Inicializando os valores
       contarAssinaturaBefore = 0
       achouBarraBefore       = False
       achouArrobaBefore      = False
       achouAspasBefore       = False
       decrementaBefore       = False
       
       achouBefore = False
       
       contarComentarioBefore = 0
       contarLetrasBefore     = 1        
       barraPraComentarioBefore       = False
       barraPraComentarioBeforeMethod = False
       barraPraComentarioBeforeEach   = False
       barraPraComentarioBeforeAll    = False
       
       barraPraComentarioBeforeSuite  = False
       barraPraComentarioBeforeClass  = False
       barraPraComentarioBeforeTest   = False
       barraPraComentarioBeforeGroups = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@ParameterizedTest' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioParameterizedTest = True
               elif (letra == '"'):
                     achouAspasParameterizedTest = True
               elif (letra == "@"):
                     flagParameterizedTest        = True
                     achouArrobaParameterizedTest = True
                     break
           
           if (barraPraComentarioParameterizedTest != True):
               if (achouAspasParameterizedTest != True):
                   contarLetrasParameterizedTest = 0
                   contarAspas                   = 0
                   naoEhParameterizedTest        = None
                   concatenarPalavras            = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagParameterizedTest == True) and (achouArrobaParameterizedTest == True)):
                               if (letra == "@"):
                                   if ((naoEhParameterizedTest == True) and (contarLetrasParameterizedTest == 18)):
                                       if ('@ParameterizedTest' == concatenarPalavras):
                                           achouAbreChaveParameterizedTest = False
                                           achouParameterizedTest          = True
                                           naoEhParameterizedTest          = False
                                           contParameterizedTest           += 1
                                           contarLetrasParameterizedTest   = 1
                                           concatenarPalavras              = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasParameterizedTest = 1
                                       achouArrobaParameterizedTest  = True
                                       concatenarPalavras            = ""
                                       
                                   contarLetrasParameterizedTest = 1
                                   concatenarPalavras            += letra
                                   
                               elif (achouArrobaParameterizedTest == True):
                                     if (contarLetrasParameterizedTest == 18):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@ParameterizedTest' == concatenarPalavras):
                                                 achouAbreChaveParameterizedTest = False
                                                 achouParameterizedTest          = True
                                                 naoEhParameterizedTest          = False
                                                 contParameterizedTest           += 1
                                                 contarLetrasParameterizedTest   = 0
                                                 concatenarPalavras              = ""
                                             if (letra == "("):
                                                 concatenarPalavras           = ""
                                                 flagParameterizedTest        = False
                                                 achouArrobaParameterizedTest = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                         
                                             contarLetrasParameterizedTest += 1
                                             naoEhParameterizedTest        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras           = ""
                                             flagParameterizedTest        = False
                                             achouArrobaParameterizedTest = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasParameterizedTest = 0
                                                 
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasParameterizedTest += 1
                                             naoEhParameterizedTest        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasParameterizedTest = True
                                   contarAspas                 += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas                 -= 2 
                                   achouAspasParameterizedTest = False
                                  
                               if (achouAspasParameterizedTest != True):
                                   if (letra == ")"):
                                       flagParameterizedTest        = True 
                                       achouArrobaParameterizedTest = True
                                   elif (letra == "@"):
                                         concatenarPalavras            = ""
                                         concatenarPalavras            += letra
                                         contarLetrasParameterizedTest = 1
                                         flagParameterizedTest         = True
                                         achouArrobaParameterizedTest  = True
                                     
                       else:
                           if ((naoEhParameterizedTest == True) and (contarLetrasParameterizedTest == 18)):
                               if ('@ParameterizedTest' == concatenarPalavras):
                                   concatenarPalavras                  = ""
                                   achouAbreChaveParameterizedTest     = False
                                   achouParameterizedTest              = True
                                   naoEhParameterizedTest              = False
                                   contParameterizedTest               += 1
                                   contarLetrasParameterizedTest       = 0
                                   barraPraComentarioParameterizedTest = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @ParameterizedTest
                   if (barraPraComentarioParameterizedTest != True):
                       if ((len("@ParameterizedTest") == contarLetrasParameterizedTest) or (len("@ParameterizedTest") == contarLetrasParameterizedTest - 1)):
                           if ('@ParameterizedTest' == concatenarPalavras):
                               concatenarPalavras              = ""
                               contarLetrasParameterizedTest   = 0
                               achouAbreChaveParameterizedTest = False
                               achouParameterizedTest          = True
                               contParameterizedTest           += 1
             
       achouArrobaParameterizedTest        = False
       achouAspasParameterizedTest         = False
       barraPraComentarioParameterizedTest = False

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@RepeatedTest' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioRepeatedTest = True
               elif (letra == '"'):
                     achouAspasRepeatedTest = True
               elif (letra == "@"):
                     flagRepeatedTest        = True
                     achouArrobaRepeatedTest = True
                     break
           
           if (barraPraComentarioRepeatedTest != True):
               if (achouAspasRepeatedTest != True):
                   contarLetrasRepeatedTest = 0
                   contarAspas              = 0
                   naoEhRepeatedTest        = None
                   concatenarPalavras       = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagRepeatedTest == True) and (achouArrobaRepeatedTest == True)):
                               if (letra == "@"):
                                   if ((naoEhRepeatedTest == True) and (contarLetrasRepeatedTest == 13)):
                                       if ('@RepeatedTest' == concatenarPalavras):
                                           achouAbreChaveRepeatedTest = False
                                           achouRepeatedTest          = True
                                           naoEhRepeatedTest          = False
                                           contRepeatedTest           += 1
                                           contarLetrasRepeatedTest   = 1
                                           concatenarPalavras         = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasRepeatedTest = 1
                                       achouArrobaRepeatedTest  = True
                                       concatenarPalavras       = ""
                                       
                                   contarLetrasRepeatedTest = 1
                                   concatenarPalavras       += letra
                                   
                               elif (achouArrobaRepeatedTest == True):
                                     if (contarLetrasRepeatedTest == 13):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@RepeatedTest' == concatenarPalavras):
                                                 achouAbreChaveRepeatedTest = False
                                                 achouRepeatedTest          = True
                                                 naoEhRepeatedTest          = False
                                                 contRepeatedTest           += 1
                                                 contarLetrasRepeatedTest   = 0
                                                 concatenarPalavras         = ""
                                             if (letra == "("):
                                                 concatenarPalavras      = ""
                                                 flagRepeatedTest        = False
                                                 achouArrobaRepeatedTest = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                         
                                             contarLetrasRepeatedTest += 1
                                             naoEhRepeatedTest        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras      = ""
                                             flagRepeatedTest        = False
                                             achouArrobaRepeatedTest = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasRepeatedTest = 0
                                                 
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasRepeatedTest += 1
                                             naoEhRepeatedTest        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasRepeatedTest = True
                                   contarAspas            += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas            -= 2
                                   achouAspasRepeatedTest = False
                                   
                               if (achouAspasRepeatedTest != True):
                                   if (letra == ")"):
                                       flagRepeatedTest        = True 
                                       achouArrobaRepeatedTest = True
                                   elif (letra == "@"):
                                         concatenarPalavras       = ""
                                         concatenarPalavras       += letra
                                         contarLetrasRepeatedTest = 1
                                         flagRepeatedTest         = True
                                         achouArrobaRepeatedTest  = True
                                     
                       else:
                           if ((naoEhRepeatedTest == True) and (contarLetrasRepeatedTest == 13)):
                               if ('@RepeatedTest' == concatenarPalavras):
                                   concatenarPalavras             = ""
                                   achouAbreChaveRepeatedTest     = False
                                   achouRepeatedTest              = True
                                   naoEhRepeatedTest              = False
                                   contRepeatedTest               += 1
                                   contarLetrasRepeatedTest       = 0
                                   barraPraComentarioRepeatedTest = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @RepeatedTest
                   if (barraPraComentarioRepeatedTest != True):
                       if ((len("@RepeatedTest") == contarLetrasRepeatedTest) or (len("@RepeatedTest") == contarLetrasRepeatedTest - 1)):
                           if ('@RepeatedTest' == concatenarPalavras):
                               concatenarPalavras         = ""
                               contarLetrasRepeatedTest   = 0
                               achouAbreChaveRepeatedTest = False
                               achouRepeatedTest          = True
                               contRepeatedTest           += 1
             
       achouArrobaRepeatedTest        = False
       achouAspasRepeatedTest         = False
       barraPraComentarioRepeatedTest = False 
       
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@TestFactory' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioTestFactory = True
               elif (letra == '"'):
                     achouAspasTestFactory = True
               elif (letra == "@"):
                     flagTestFactory        = True
                     achouArrobaTestFactory = True
                     break
           
           if (barraPraComentarioTestFactory != True):
               if (achouAspasTestFactory != True):
                   contarLetrasTestFactory = 0
                   contarAspas             = 0
                   naoEhTestFactory        = None
                   concatenarPalavras      = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagTestFactory == True) and (achouArrobaTestFactory == True)):
                               if (letra == "@"):
                                   if ((naoEhTestFactory == True) and (contarLetrasTestFactory == 12)):
                                       if ('@TestFactory' == concatenarPalavras):
                                           achouAbreChaveTestFactory = False
                                           achouTestFactory          = True
                                           naoEhTestFactory          = False
                                           contTestFactory           += 1
                                           contarLetrasTestFactory   = 1
                                           concatenarPalavras        = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasTestFactory = 1
                                       achouArrobaTestFactory  = True
                                       concatenarPalavras      = ""
                                       
                                   contarLetrasTestFactory = 1
                                   concatenarPalavras      += letra
                                   
                               elif (achouArrobaTestFactory == True):
                                     if (contarLetrasTestFactory == 12):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@TestFactory' == concatenarPalavras):
                                                 achouAbreChaveTestFactory = False
                                                 achouTestFactory          = True
                                                 naoEhTestFactory          = False
                                                 contTestFactory           += 1
                                                 contarLetrasTestFactory   = 0
                                                 concatenarPalavras        = ""
                                             if (letra == "("):
                                                 concatenarPalavras     = ""
                                                 flagTestFactory        = False
                                                 achouArrobaTestFactory = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasTestFactory += 1
                                             naoEhTestFactory        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras     = ""
                                             flagTestFactory        = False
                                             achouArrobaTestFactory = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasTestFactory = 0
                                                 
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasTestFactory += 1
                                             naoEhTestFactory        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasTestFactory = True
                                   contarAspas           += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas           -= 2
                                   achouAspasTestFactory = False
                                   
                               if (achouAspasTestFactory != True):
                                   if (letra == ")"):
                                       flagTestFactory        = True 
                                       achouArrobaTestFactory = True
                                   elif (letra == "@"):
                                         concatenarPalavras      = ""
                                         concatenarPalavras      += letra
                                         contarLetrasTestFactory = 1
                                         flagTestFactory         = True
                                         achouArrobaTestFactory  = True
                                     
                       else:
                           if ((naoEhTestFactory == True) and (contarLetrasTestFactory == 12)):
                               if ('@TestFactory' == concatenarPalavras):
                                   concatenarPalavras            = ""
                                   achouAbreChaveTestFactory     = False
                                   achouTestFactory              = True
                                   naoEhTestFactory              = False
                                   contTestFactory               += 1
                                   contarLetrasTestFactory       = 0
                                   barraPraComentarioTestFactory = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @TestFactory
                   if (barraPraComentarioTestFactory != True):
                       if ((len("@TestFactory") == contarLetrasTestFactory) or (len("@TestFactory") == contarLetrasTestFactory - 1)):
                           if ('@TestFactory' == concatenarPalavras):
                               concatenarPalavras        = ""
                               contarLetrasTestFactory   = 0
                               achouAbreChaveTestFactory = False
                               achouTestFactory          = True
                               contTestFactory           += 1
             
       achouArrobaTestFactory        = False
       achouAspasTestFactory         = False
       barraPraComentarioTestFactory = False
   
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@TestTemplate' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioTestTemplate = True
               elif (letra == '"'):
                     achouAspasTestTemplate = True
               elif (letra == "@"):
                     flagTestTemplate        = True
                     achouArrobaTestTemplate = True
                     break
           
           if (barraPraComentarioTestTemplate != True):
               if (achouAspasTestTemplate != True):
                   contarLetrasTestTemplate = 0
                   contarAspas              = 0
                   naoEhTestTemplate        = None
                   concatenarPalavras       = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagTestTemplate == True) and (achouArrobaTestTemplate == True)):
                               if (letra == "@"):
                                   if ((naoEhTestTemplate == True) and (contarLetrasTestTemplate == 13)):
                                       if ('@TestTemplate' == concatenarPalavras):
                                           achouAbreChaveTestTemplate = False
                                           achouTestTemplate          = True
                                           naoEhTestTemplate          = False
                                           contTestTemplate           += 1
                                           contarLetrasTestTemplate   = 1
                                           concatenarPalavras         = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasTestTemplate = 1
                                       achouArrobaTestTemplate  = True
                                       concatenarPalavras       = ""
                                   
                                   contarLetrasTestTemplate = 1
                                   concatenarPalavras       += letra
                                   
                               elif (achouArrobaTestTemplate == True):
                                     if (contarLetrasTestTemplate == 13):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@TestTemplate' == concatenarPalavras):
                                                 achouAbreChaveTestTemplate = False
                                                 achouTestTemplate          = True
                                                 naoEhTestTemplate          = False
                                                 contTestTemplate           += 1
                                                 contarLetrasTestTemplate   = 0
                                                 concatenarPalavras         = ""
                                             if (letra == "("):
                                                 concatenarPalavras      = ""
                                                 flagTestTemplate        = False
                                                 achouArrobaTestTemplate = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                         
                                             contarLetrasTestTemplate += 1
                                             naoEhTestTemplate        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras      = ""
                                             flagTestTemplate        = False
                                             achouArrobaTestTemplate = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasTestTemplate = 0
                                                 
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasTestTemplate += 1
                                             naoEhTestTemplate        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasTestTemplate = True
                                   contarAspas            += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas            -= 2
                                   achouAspasTestTemplate = False
                                   
                               if (achouAspasTestTemplate != True):
                                   if (letra == ")"):
                                       flagTestTemplate        = True 
                                       achouArrobaTestTemplate = True
                                   elif (letra == "@"):
                                         concatenarPalavras       = ""
                                         concatenarPalavras       += letra
                                         contarLetrasTestTemplate = 1
                                         flagTestTemplate         = True
                                         achouArrobaTestTemplate  = True
                               else:
                                   if (letra == ")"):
                                       flagTestTemplate        = True 
                                       achouArrobaTestTemplate = True
                                     
                       else:
                           if ((naoEhTestTemplate == True) and (contarLetrasTestTemplate == 13)):
                               if ('@TestTemplate' == concatenarPalavras):
                                   concatenarPalavras             = ""
                                   achouAbreChaveTestTemplate     = False
                                   achouTestTemplate              = True
                                   naoEhTestTemplate              = False
                                   contTestTemplate               += 1
                                   contarLetrasTestTemplate       = 0
                                   barraPraComentarioTestTemplate = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @TestTemplate
                   if (barraPraComentarioTestTemplate != True):
                       if ((len("@TestTemplate") == contarLetrasTestTemplate) or (len("@TestTemplate") == contarLetrasTestTemplate - 1)):
                           if ('@TestTemplate' == concatenarPalavras):
                               concatenarPalavras         = ""
                               contarLetrasTestTemplate   = 0
                               achouAbreChaveTestTemplate = False
                               achouTestTemplate          = True
                               contTestTemplate           += 1
             
       achouArrobaTestTemplate        = False
       achouAspasTestTemplate         = False
       barraPraComentarioTestTemplate = False

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@TestMethodOrder' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioTestMethodOrder = True
               elif (letra == '"'):
                     achouAspasTestMethodOrder = True
               elif (letra == "@"):
                     flagTestMethodOrder        = True
                     achouArrobaTestMethodOrder = True
                     break
           
           if (barraPraComentarioTestMethodOrder != True):
               if (achouAspasTestMethodOrder != True):
                   contarLetrasTestMethodOrder = 0
                   contarAspas                 = 0
                   naoEhTestMethodOrder        = None
                   concatenarPalavras          = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagTestMethodOrder == True) and (achouArrobaTestMethodOrder == True)):
                               if (letra == "@"):
                                   if ((naoEhTestMethodOrder == True) and (contarLetrasTestMethodOrder == 16)):
                                       if ('@TestMethodOrder' == concatenarPalavras):
                                           achouAbreChaveTestMethodOrder = False
                                           achouTestMethodOrder          = True
                                           naoEhTestMethodOrder          = False
                                           contTestMethodOrder           += 1
                                           contarLetrasTestMethodOrder   = 1
                                           concatenarPalavras            = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasTestMethodOrder = 1
                                       achouArrobaTestMethodOrder  = True
                                       concatenarPalavras          = ""
                                       
                                   contarLetrasTestMethodOrder = 1
                                   concatenarPalavras          += letra
                                   
                               elif (achouArrobaTestMethodOrder == True):
                                     if (contarLetrasTestMethodOrder == 16):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@TestMethodOrder' == concatenarPalavras):
                                                 achouAbreChaveTestMethodOrder = False
                                                 achouTestMethodOrder          = True
                                                 naoEhTestMethodOrder          = False
                                                 contTestMethodOrder           += 1
                                                 contarLetrasTestMethodOrder   = 0
                                                 concatenarPalavras            = ""
                                             if (letra == "("):
                                                 concatenarPalavras         = ""
                                                 flagTestMethodOrder        = False
                                                 achouArrobaTestMethodOrder = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                         
                                             contarLetrasTestMethodOrder += 1
                                             naoEhTestMethodOrder        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras         = ""
                                             flagTestMethodOrder        = False
                                             achouArrobaTestMethodOrder = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasTestMethodOrder = 0
                                                 
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasTestMethodOrder += 1
                                             naoEhTestMethodOrder        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasTestMethodOrder = True
                                   contarAspas               += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas               -= 2
                                   achouAspasTestMethodOrder = False
                                   
                               if (achouAspasTestMethodOrder != True):
                                   if (letra == ")"):
                                       flagTestMethodOrder        = True 
                                       achouArrobaTestMethodOrder = True
                                   elif (letra == "@"):
                                         concatenarPalavras          = ""
                                         concatenarPalavras          += letra
                                         contarLetrasTestMethodOrder = 1
                                         flagTestMethodOrder         = True
                                         achouArrobaTestMethodOrder  = True
                                     
                       else:
                           if ((naoEhTestMethodOrder == True) and (contarLetrasTestMethodOrder == 16)):
                               if ('@TestMethodOrder' == concatenarPalavras):
                                   concatenarPalavras                = ""
                                   achouAbreChaveTestMethodOrder     = False
                                   achouTestMethodOrder              = True
                                   naoEhTestMethodOrder              = False
                                   contTestMethodOrder               += 1
                                   contarLetrasTestMethodOrder       = 0
                                   barraPraComentarioTestMethodOrder = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @TestMethodOrder
                   if (barraPraComentarioTestMethodOrder != True):
                       if ((len("@TestMethodOrder") == contarLetrasTestMethodOrder) or (len("@TestMethodOrder") == contarLetrasTestMethodOrder - 1)):
                           if ('@TestMethodOrder' == concatenarPalavras):
                               concatenarPalavras            = ""
                               contarLetrasTestMethodOrder   = 0
                               achouAbreChaveTestMethodOrder = False
                               achouTestMethodOrder          = True
                               contTestMethodOrder           += 1
             
       achouArrobaTestMethodOrder        = False
       achouAspasTestMethodOrder         = False
       barraPraComentarioTestMethodOrder = False
   
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@TestInstance' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioTestInstance = True
               elif (letra == '"'):
                     achouAspasTestInstance = True
               elif (letra == "@"):
                     flagTestInstance        = True
                     achouArrobaTestInstance = True
                     break
           
           if (barraPraComentarioTestInstance != True):
               if (achouAspasTestInstance != True):
                   contarLetrasTestInstance = 0
                   contarAspas              = 0
                   naoEhTestInstance        = None
                   concatenarPalavras       = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagTestInstance == True) and (achouArrobaTestInstance == True)):
                               if (letra == "@"):
                                   if ((naoEhTestInstance == True) and (contarLetrasTestInstance == 13)):
                                       if ('@TestInstance' == concatenarPalavras):
                                           achouAbreChaveTestInstance = False
                                           achouTestInstance          = True
                                           naoEhTestInstance          = False
                                           contTestInstance           += 1
                                           contarLetrasTestInstance   = 1
                                           concatenarPalavras         = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasTestInstance = 1
                                       achouArrobaTestInstance  = True
                                       concatenarPalavras       = ""
                                       
                                   contarLetrasTestInstance = 1
                                   concatenarPalavras       += letra
                                   
                               elif (achouArrobaTestInstance == True):
                                     if (contarLetrasTestInstance == 13):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@TestInstance' == concatenarPalavras):
                                                 achouAbreChaveTestInstance = False
                                                 achouTestInstance          = True
                                                 naoEhTestInstance          = False
                                                 contTestInstance           += 1
                                                 contarLetrasTestInstance   = 0
                                                 concatenarPalavras         = ""
                                             if (letra == "("):
                                                 concatenarPalavras      = ""
                                                 flagTestInstance        = False
                                                 achouArrobaTestInstance = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                         
                                             contarLetrasTestInstance += 1
                                             naoEhTestInstance        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras      = ""
                                             flagTestInstance        = False
                                             achouArrobaTestInstance = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasTestInstance = 0
                                              
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                              
                                             contarLetrasTestInstance += 1
                                             naoEhTestInstance        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasTestInstance = True
                                   contarAspas            += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas            -= 2
                                   achouAspasTestInstance = False
                                   
                               if (achouAspasTestInstance != True):
                                   if (letra == ")"):
                                       flagTestInstance        = True 
                                       achouArrobaTestInstance = True
                                   elif (letra == "@"):
                                         concatenarPalavras       = ""
                                         concatenarPalavras       += letra
                                         contarLetrasTestInstance = 1
                                         flagTestInstance         = True
                                         achouArrobaTestInstance  = True
                                     
                       else:
                           if ((naoEhTestInstance == True) and (contarLetrasTestInstance == 13)):
                               if ('@TestInstance' == concatenarPalavras):
                                   concatenarPalavras             = ""
                                   achouAbreChaveTestInstance     = False
                                   achouTestInstance              = True
                                   naoEhTestInstance              = False
                                   contTestInstance               += 1
                                   contarLetrasTestInstance       = 0
                                   barraPraComentarioTestInstance = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @TestInstance
                   if (barraPraComentarioTestInstance != True):
                       if ((len("@TestInstance") == contarLetrasTestInstance) or (len("@TestInstance") == contarLetrasTestInstance - 1)):
                           if ('@TestInstance' == concatenarPalavras):
                               concatenarPalavras         = ""
                               contarLetrasTestInstance   = 0
                               achouAbreChaveTestInstance = False
                               achouTestInstance          = True
                               contTestInstance           += 1
             
       achouArrobaTestInstance        = False
       achouAspasTestInstance         = False
       barraPraComentarioTestInstance = False                 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@DisplayName' in line:
           tamanho = (len(line) - 1)
           for letra in line:
               if (letra == "/"):
                   barraPraComentarioDisplayName = True
               elif (letra == "@"):
                     break
                     
           if '@DisplayNameGeneration' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioDisplayNameGeneration = True
                   elif (letra == "@"):
                         break
                         
           if (barraPraComentarioDisplayName != barraPraComentarioDisplayNameGeneration):
               for letra in line:
                   if (letra == "/"):
                       contarComentarioDisplayName += 1
                   elif (letra == " ") or (letra == "	"):
                         contarComentarioDisplayName += 1
                   else:
                       if (contarLetrasDisplayName <= 12):
                           contarLetrasDisplayName += 1
                       else:
                           contarComentarioDisplayName += 1

           if (len("@DisplayName") != (tamanho - (contarComentarioDisplayName - 1)) and (barraPraComentarioDisplayName == False)):
               for letra in line:
                   if ((letra == " ")or(letra == "	")):
                       contarAssinaturaDisplayName += 1
                   elif (letra == "/"):
                         contarAssinaturaDisplayName += 1
        
               for letra in line:
                   if (letra == "/"):
                       achouBarraDisplayName = True
                   elif (achouBarraDisplayName == True):
                         if ((letra != " ")and(letra != "	")):
                             contarAssinaturaDisplayName += 1
                             decrementaDisplayName       = True
                        
               if (decrementaDisplayName == True):
                   if (len("@DisplayName") == (tamanho - (contarAssinaturaDisplayName - 1))):
                       achouAbreChaveDisplayName = False
                       achouDisplayName          = True
                       contDisplayName           += 1
               else:
                   if (len("@DisplayName") == (tamanho - contarAssinaturaDisplayName)):
                       achouAbreChaveDisplayName = False
                       achouDisplayName          = True
                       contDisplayName           += 1

               if (achouDisplayName != True):
                   contarLetrasDisplayName = 0
                   contarAspas             = 0
                   naoEhDisplayName        = None
                   concatenarPalavras      = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagDisplayName == True) and (achouArrobaDisplayName == True)):
                               if (letra == "@"):
                                   if ((naoEhDisplayName == True) and (contarLetrasDisplayName == 12)):
                                       if ('@DisplayName' == concatenarPalavras):
                                           achouAbreChaveDisplayName = False
                                           achouDisplayName          = True
                                           naoEhDisplayName          = False
                                           contDisplayName           += 1
                                           contarLetrasDisplayName   = 1
                                           concatenarPalavras        = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasDisplayName = 1
                                       achouArrobaDisplayName  = True
                                       concatenarPalavras      = ""
                                   
                                   contarLetrasDisplayName = 1
                                   concatenarPalavras      += letra
                                   
                               elif (achouArrobaDisplayName == True):
                                     if (contarLetrasDisplayName == 12):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@DisplayName' == concatenarPalavras):
                                                 achouAbreChaveDisplayName = False
                                                 achouDisplayName          = True
                                                 naoEhDisplayName          = False
                                                 contDisplayName           += 1
                                                 contarLetrasDisplayName   = 0
                                                 concatenarPalavras        = ""
                                             if (letra == "("):
                                                 concatenarPalavras     = ""
                                                 flagDisplayName        = False
                                                 achouArrobaDisplayName = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasDisplayName += 1
                                             naoEhDisplayName        = False
                                             
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras     = ""
                                             flagDisplayName        = False
                                             achouArrobaDisplayName = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasDisplayName = 0
                                             
                                             if ((letra != " ")and(letra != "   ")):                                             
                                                 concatenarPalavras += letra
                                             
                                             contarLetrasDisplayName += 1
                                             naoEhDisplayName        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasDisplayName = True
                                   contarAspas           += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas           -= 2
                                   achouAspasDisplayName = False
                                   
                               if (achouAspasDisplayName != True):
                                   if (letra == ")"):
                                       flagDisplayName        = True 
                                       achouArrobaDisplayName = True
                                   elif (letra == "@"):
                                         concatenarPalavras      = ""
                                         concatenarPalavras      += letra
                                         contarLetrasDisplayName = 1
                                         flagDisplayName         = True
                                         achouArrobaDisplayName  = True
                                     
                       else:
                           if ((naoEhDisplayName == True) and (contarLetrasDisplayName == 12)):
                               if ('@DisplayName' == concatenarPalavras):
                                   concatenarPalavras            = ""
                                   achouAbreChaveDisplayName     = False
                                   achouDisplayName              = True
                                   naoEhDisplayName              = False
                                   contDisplayName               += 1
                                   contarLetrasDisplayName       = 0
                                   barraPraComentarioDisplayName = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @DisplayName
                   if (barraPraComentarioDisplayName != True):
                       if ((len("@DisplayName") == contarLetrasDisplayName) or (len("@DisplayName") == contarLetrasDisplayName - 1)):
                           if ('@DisplayName' == concatenarPalavras):
                               concatenarPalavras        = ""
                               contarLetrasDisplayName   = 0
                               achouAbreChaveDisplayName = False
                               achouDisplayName          = True
                               contDisplayName           += 1
       
       #Inicializando os valores
       contarAssinaturaDisplayName = 0
       achouBarraDisplayName       = False
       achouArrobaDisplayName      = False
       achouAspasDisplayName       = False
       decrementaDisplayName       = False
       
       achouDisplayName = False
       
       contarComentarioDisplayName = 0
       contarLetrasDisplayName     = 1
       barraPraComentarioDisplayName           = False
       barraPraComentarioDisplayNameGeneration = False

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@DisplayNameGeneration' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioDisplayNameGeneration = True
               elif (letra == '"'):
                     achouAspasDisplayNameGeneration = True
               elif (letra == "@"):
                     flagDisplayNameGeneration        = True
                     achouArrobaDisplayNameGeneration = True
                     break
           
           if (barraPraComentarioDisplayNameGeneration != True):
               if (achouAspasDisplayNameGeneration != True):
                   contarLetrasDisplayNameGeneration = 0
                   contarAspas                       = 0
                   naoEhDisplayNameGeneration        = None
                   concatenarPalavras                = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagDisplayNameGeneration == True) and (achouArrobaDisplayNameGeneration == True)):
                               if (letra == "@"):
                                   if ((naoEhDisplayNameGeneration == True) and (contarLetrasDisplayNameGeneration == 22)):
                                       if ('@DisplayNameGeneration' == concatenarPalavras):
                                           achouAbreChaveDisplayNameGeneration = False
                                           achouDisplayNameGeneration          = True
                                           naoEhDisplayNameGeneration          = False
                                           contDisplayNameGeneration           += 1
                                           contarLetrasDisplayNameGeneration   = 1
                                           concatenarPalavras = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasDisplayNameGeneration = 1
                                       achouArrobaDisplayNameGeneration  = True
                                       concatenarPalavras                = ""
                                   
                                   contarLetrasDisplayNameGeneration = 1
                                   concatenarPalavras                += letra
                                   
                               elif (achouArrobaDisplayNameGeneration == True):
                                     if (contarLetrasDisplayNameGeneration == 22):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@DisplayNameGeneration' == concatenarPalavras):
                                                 achouAbreChaveDisplayNameGeneration = False
                                                 achouDisplayNameGeneration          = True
                                                 naoEhDisplayNameGeneration          = False
                                                 contDisplayNameGeneration           += 1
                                                 contarLetrasDisplayNameGeneration   = 0
                                                 concatenarPalavras                  = ""
                                             if (letra == "("):
                                                 concatenarPalavras               = ""
                                                 flagDisplayNameGeneration        = False
                                                 achouArrobaDisplayNameGeneration = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                         
                                             contarLetrasDisplayNameGeneration += 1
                                             naoEhDisplayNameGeneration        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras               = ""
                                             flagDisplayNameGeneration        = False
                                             achouArrobaDisplayNameGeneration = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasDisplayNameGeneration = 0
                                                 
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasDisplayNameGeneration += 1
                                             naoEhDisplayNameGeneration        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasDisplayNameGeneration = True
                                   contarAspas                     += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas                     -= 2
                                   achouAspasDisplayNameGeneration = False
                                   
                               if (achouAspasDisplayNameGeneration != True):
                                   if (letra == ")"):
                                       flagDisplayNameGeneration        = True 
                                       achouArrobaDisplayNameGeneration = True
                                   elif (letra == "@"):
                                         concatenarPalavras = ""
                                         concatenarPalavras                += letra
                                         contarLetrasDisplayNameGeneration = 1
                                         flagDisplayNameGeneration         = True
                                         achouArrobaDisplayNameGeneration  = True
                                     
                       else:
                           if ((naoEhDisplayNameGeneration == True) and (contarLetrasDisplayNameGeneration == 22)):
                               if ('@DisplayNameGeneration' == concatenarPalavras):
                                   concatenarPalavras                      = ""
                                   achouAbreChaveDisplayNameGeneration     = False
                                   achouDisplayNameGeneration              = True
                                   naoEhDisplayNameGeneration              = False
                                   contDisplayNameGeneration               += 1
                                   contarLetrasDisplayNameGeneration       = 0
                                   barraPraComentarioDisplayNameGeneration = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @DisplayNameGeneration
                   if (barraPraComentarioDisplayNameGeneration != True):
                       if ((len("@DisplayNameGeneration") == contarLetrasDisplayNameGeneration) or (len("@DisplayNameGeneration") == contarLetrasDisplayNameGeneration - 1)):
                           if ('@DisplayNameGeneration' == concatenarPalavras):
                               concatenarPalavras                  = ""
                               contarLetrasDisplayNameGeneration   = 0
                               achouAbreChaveDisplayNameGeneration = False
                               achouDisplayNameGeneration          = True
                               contDisplayNameGeneration           += 1
             
       achouArrobaDisplayNameGeneration        = False
       achouAspasDisplayNameGeneration         = False
       barraPraComentarioDisplayNameGeneration = False 
   
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@BeforeEach' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioBeforeEach = True
               elif (letra == '"'):
                     achouAspasBeforeEach = True
               elif (letra == "@"):
                     flagBeforeEach        = True
                     achouArrobaBeforeEach = True
                     break
           
           if (barraPraComentarioBeforeEach != True):
               if (achouAspasBeforeEach != True):
                   contarLetrasBeforeEach = 0
                   contarAspas            = 0
                   naoEhBeforeEach        = None
                   concatenarPalavras     = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagBeforeEach == True) and (achouArrobaBeforeEach == True)):
                               if (letra == "@"):
                                   if ((naoEhBeforeEach == True) and (contarLetrasBeforeEach == 11)):
                                       if ('@BeforeEach' == concatenarPalavras):
                                           achouAbreChaveBeforeEach = False
                                           achouBeforeEach          = True
                                           naoEhBeforeEach          = False
                                           contBeforeEach           += 1
                                           contarLetrasBeforeEach   = 1
                                           concatenarPalavras       = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasBeforeEach = 1
                                       achouArrobaBeforeEach  = True
                                       concatenarPalavras     = ""
                                       
                                   contarLetrasBeforeEach = 1
                                   concatenarPalavras     += letra
                                   
                               elif (achouArrobaBeforeEach == True):
                                     if (contarLetrasBeforeEach == 11):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@BeforeEach' == concatenarPalavras):
                                                 achouAbreChaveBeforeEach = False
                                                 achouBeforeEach          = True
                                                 naoEhBeforeEach          = False
                                                 contBeforeEach           += 1
                                                 contarLetrasBeforeEach   = 0
                                                 concatenarPalavras       = ""
                                             if (letra == "("):
                                                 concatenarPalavras    = ""
                                                 flagBeforeEach        = False
                                                 achouArrobaBeforeEach = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                         
                                             contarLetrasBeforeEach += 1
                                             naoEhBeforeEach        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras    = ""
                                             flagBeforeEach        = False
                                             achouArrobaBeforeEach = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasBeforeEach = 0
                                                 
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasBeforeEach += 1
                                             naoEhBeforeEach        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasBeforeEach = True
                                   contarAspas          += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas          -= 2
                                   achouAspasBeforeEach = False
                                   
                               if (achouAspasBeforeEach != True):
                                   if (letra == ")"):
                                       flagBeforeEach        = True 
                                       achouArrobaBeforeEach = True
                                   elif (letra == "@"):
                                         concatenarPalavras     = ""
                                         concatenarPalavras     += letra
                                         contarLetrasBeforeEach = 1
                                         flagBeforeEach         = True
                                         achouArrobaBeforeEach  = True
                                     
                       else:
                           if ((naoEhBeforeEach == True) and (contarLetrasBeforeEach == 11)):
                               if ('@BeforeEach' == concatenarPalavras):
                                   concatenarPalavras           = ""
                                   achouAbreChaveBeforeEach     = False
                                   achouBeforeEach              = True
                                   naoEhBeforeEach              = False
                                   contBeforeEach               += 1
                                   contarLetrasBeforeEach       = 0
                                   barraPraComentarioBeforeEach = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @BeforeEach
                   if (barraPraComentarioBeforeEach != True):
                       if ((len("@BeforeEach") == contarLetrasBeforeEach) or (len("@BeforeEach") == contarLetrasBeforeEach - 1)):
                           if ('@BeforeEach' == concatenarPalavras):
                               concatenarPalavras       = ""
                               contarLetrasBeforeEach   = 0
                               achouAbreChaveBeforeEach = False
                               achouBeforeEach          = True
                               contBeforeEach           += 1
             
       achouArrobaBeforeEach        = False
       achouAspasBeforeEach         = False
       barraPraComentarioBeforeEach = False

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@AfterEach' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioAfterEach = True
               elif (letra == '"'):
                     achouAspasAfterEach = True
               elif (letra == "@"):
                     flagAfterEach        = True
                     achouArrobaAfterEach = True
                     break
           
           if (barraPraComentarioAfterEach != True):
               if (achouAspasAfterEach != True):
                   contarLetrasAfterEach = 0
                   contarAspas           = 0
                   naoEhAfterEach        = None
                   concatenarPalavras    = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagAfterEach == True) and (achouArrobaAfterEach == True)):
                               if (letra == "@"):
                                   if ((naoEhAfterEach == True) and (contarLetrasAfterEach == 10)):
                                       if ('@AfterEach' == concatenarPalavras):
                                           achouAbreChaveAfterEach = False
                                           achouAfterEach          = True
                                           naoEhAfterEach          = False
                                           contAfterEach           += 1
                                           contarLetrasAfterEach   = 1
                                           concatenarPalavras      = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasAfterEach = 1
                                       achouArrobaAfterEach  = True
                                       concatenarPalavras    = ""
                                       
                                   contarLetrasAfterEach = 1
                                   concatenarPalavras    += letra
                                   
                               elif (achouArrobaAfterEach == True):
                                     if (contarLetrasAfterEach == 10):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@AfterEach' == concatenarPalavras):
                                                 achouAbreChaveAfterEach = False
                                                 achouAfterEach          = True
                                                 naoEhAfterEach          = False
                                                 contAfterEach           += 1
                                                 contarLetrasAfterEach   = 0
                                                 concatenarPalavras      = ""
                                             if (letra == "("):
                                                 concatenarPalavras   = ""
                                                 flagAfterEach        = False
                                                 achouArrobaAfterEach = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                         
                                             contarLetrasAfterEach += 1
                                             naoEhAfterEach        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras   = ""
                                             flagAfterEach        = False
                                             achouArrobaAfterEach = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasAfterEach = 0
                                              
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                              
                                             contarLetrasAfterEach += 1
                                             naoEhAfterEach        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasAfterEach = True
                                   contarAspas         += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas         -= 2
                                   achouAspasAfterEach = False
                                   
                               if (achouAspasAfterEach != True):
                                   if (letra == ")"):
                                       flagAfterEach        = True 
                                       achouArrobaAfterEach = True
                                   elif (letra == "@"):
                                         concatenarPalavras    = ""
                                         concatenarPalavras    += letra
                                         contarLetrasAfterEach = 1
                                         flagAfterEach         = True
                                         achouArrobaAfterEach  = True
                                     
                       else:
                           if ((naoEhAfterEach == True) and (contarLetrasAfterEach == 10)):
                               if ('@AfterEach' == concatenarPalavras):
                                   concatenarPalavras          = ""
                                   achouAbreChaveAfterEach     = False
                                   achouAfterEach              = True
                                   naoEhAfterEach              = False
                                   contAfterEach               += 1
                                   contarLetrasAfterEach       = 0
                                   barraPraComentarioAfterEach = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @AfterEach
                   if (barraPraComentarioAfterEach != True):
                       if ((len("@AfterEach") == contarLetrasAfterEach) or (len("@AfterEach") == contarLetrasAfterEach - 1)):
                           if ('@AfterEach' == concatenarPalavras):
                               concatenarPalavras      = ""
                               contarLetrasAfterEach   = 0
                               achouAbreChaveAfterEach = False
                               achouAfterEach          = True
                               contAfterEach           += 1
             
       achouArrobaAfterEach        = False
       achouAspasAfterEach         = False
       barraPraComentarioAfterEach = False
       
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@BeforeAll' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioBeforeAll = True
               elif (letra == '"'):
                     achouAspasBeforeAll = True
               elif (letra == "@"):
                     flagBeforeAll        = True
                     achouArrobaBeforeAll = True
                     break
           
           if (barraPraComentarioBeforeAll != True):
               if (achouAspasBeforeAll != True):
                   contarLetrasBeforeAll = 0
                   contarAspas           = 0
                   naoEhBeforeAll        = None
                   concatenarPalavras    = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagBeforeAll == True) and (achouArrobaBeforeAll == True)):
                               if (letra == "@"):
                                   if ((naoEhBeforeAll == True) and (contarLetrasBeforeAll == 10)):
                                       if ('@BeforeAll' == concatenarPalavras):
                                           achouAbreChaveBeforeAll = False
                                           achouBeforeAll          = True
                                           naoEhBeforeAll          = False
                                           contBeforeAll           += 1
                                           contarLetrasBeforeAll   = 1
                                           concatenarPalavras      = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasBeforeAll = 1
                                       achouArrobaBeforeAll  = True
                                       concatenarPalavras    = ""
                                       
                                   contarLetrasBeforeAll = 1
                                   concatenarPalavras    += letra
                                   
                               elif (achouArrobaBeforeAll == True):
                                     if (contarLetrasBeforeAll == 10):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@BeforeAll' == concatenarPalavras):
                                                 achouAbreChaveBeforeAll = False
                                                 achouBeforeAll          = True
                                                 naoEhBeforeAll          = False
                                                 contBeforeAll           += 1
                                                 contarLetrasBeforeAll   = 0
                                                 concatenarPalavras      = ""
                                             if (letra == "("):
                                                 concatenarPalavras   = ""
                                                 flagBeforeAll        = False
                                                 achouArrobaBeforeAll = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                         
                                             contarLetrasBeforeAll += 1
                                             naoEhBeforeAll        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras   = ""
                                             flagBeforeAll        = False
                                             achouArrobaBeforeAll = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasBeforeAll = 0
                                                 
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasBeforeAll += 1
                                             naoEhBeforeAll        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasBeforeAll = True
                                   contarAspas         += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas         -= 2
                                   achouAspasBeforeAll = False
                                   
                               if (achouAspasBeforeAll != True):
                                   if (letra == ")"):
                                       flagBeforeAll        = True 
                                       achouArrobaBeforeAll = True
                                   elif (letra == "@"):
                                         concatenarPalavras    = ""
                                         concatenarPalavras    += letra
                                         contarLetrasBeforeAll = 1
                                         flagBeforeAll         = True
                                         achouArrobaBeforeAll  = True
                                     
                       else:
                           if ((naoEhBeforeAll == True) and (contarLetrasBeforeAll == 10)):
                               if ('@BeforeAll' == concatenarPalavras):
                                   concatenarPalavras          = ""
                                   achouAbreChaveBeforeAll     = False
                                   achouBeforeAll              = True
                                   naoEhBeforeAll              = False
                                   contBeforeAll               += 1
                                   contarLetrasBeforeAll       = 0
                                   barraPraComentarioBeforeAll = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @BeforeAll
                   if (barraPraComentarioBeforeAll != True):
                       if ((len("@BeforeAll") == contarLetrasBeforeAll) or (len("@BeforeAll") == contarLetrasBeforeAll - 1)):
                           if ('@BeforeAll' == concatenarPalavras):
                               concatenarPalavras      = ""
                               contarLetrasBeforeAll   = 0
                               achouAbreChaveBeforeAll = False
                               achouBeforeAll          = True
                               contBeforeAll           += 1
             
       achouArrobaBeforeAll        = False
       achouAspasBeforeAll         = False
       barraPraComentarioBeforeAll = False
       
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@AfterAll' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioAfterAll = True
               elif (letra == '"'):
                     achouAspasAfterAll = True
               elif (letra == "@"):
                     flagAfterAll        = True
                     achouArrobaAfterAll = True
                     break
           
           if (barraPraComentarioAfterAll != True):
               if (achouAspasAfterAll != True):
                   contarLetrasAfterAll = 0
                   contarAspas          = 0
                   naoEhAfterAll        = None
                   concatenarPalavras   = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagAfterAll == True) and (achouArrobaAfterAll == True)):
                               if (letra == "@"):
                                   if ((naoEhAfterAll == True) and (contarLetrasAfterAll == 9)):
                                       if ('@AfterAll' == concatenarPalavras):
                                           achouAbreChaveAfterAll = False
                                           achouAfterAll          = True
                                           naoEhAfterAll          = False
                                           contAfterAll           += 1
                                           contarLetrasAfterAll   = 1
                                           concatenarPalavras     = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasAfterAll = 1
                                       achouArrobaAfterAll  = True
                                       concatenarPalavras   = ""
                                       
                                   contarLetrasAfterAll = 1
                                   concatenarPalavras   += letra
                                   
                               elif (achouArrobaAfterAll == True):
                                     if (contarLetrasAfterAll == 9):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@AfterAll' == concatenarPalavras):
                                                 achouAbreChaveAfterAll = False
                                                 achouAfterAll          = True
                                                 naoEhAfterAll          = False
                                                 contAfterAll           += 1
                                                 contarLetrasAfterAll   = 0
                                                 concatenarPalavras     = ""
                                             if (letra == "("):
                                                 concatenarPalavras  = ""
                                                 flagAfterAll        = False
                                                 achouArrobaAfterAll = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                         
                                             contarLetrasAfterAll += 1
                                             naoEhAfterAll        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras  = ""
                                             flagAfterAll        = False
                                             achouArrobaAfterAll = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasAfterAll = 0
                                                 
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasAfterAll += 1
                                             naoEhAfterAll        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasAfterAll = True
                                   contarAspas        += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas        -= 2
                                   achouAspasAfterAll = False
                                   
                               if (achouAspasAfterAll != True):
                                   if (letra == ")"):
                                       flagAfterAll        = True 
                                       achouArrobaAfterAll = True
                                   elif (letra == "@"):
                                         concatenarPalavras   = ""
                                         concatenarPalavras   += letra
                                         contarLetrasAfterAll = 1
                                         flagAfterAll         = True
                                         achouArrobaAfterAll  = True
                                     
                       else:
                           if ((naoEhAfterAll == True) and (contarLetrasAfterAll == 9)):
                               if ('@AfterAll' == concatenarPalavras):
                                   concatenarPalavras         = ""
                                   achouAbreChaveAfterAll     = False
                                   achouAfterAll              = True
                                   naoEhAfterAll              = False
                                   contAfterAll               += 1
                                   contarLetrasAfterAll       = 0
                                   barraPraComentarioAfterAll = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @AfterAll
                   if (barraPraComentarioAfterAll != True):
                       if ((len("@AfterAll") == contarLetrasAfterAll) or (len("@AfterAll") == contarLetrasAfterAll - 1)):
                           if ('@AfterAll' == concatenarPalavras):
                               concatenarPalavras     = ""
                               contarLetrasAfterAll   = 0
                               achouAbreChaveAfterAll = False
                               achouAfterAll          = True
                               contAfterAll           += 1
             
       achouArrobaAfterAll        = False
       achouAspasAfterAll         = False
       barraPraComentarioAfterAll = False
   
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@Nested' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioNested = True
               elif (letra == '"'):
                     achouAspasNested = True
               elif (letra == "@"):
                     flagNested        = True
                     achouArrobaNested = True
                     break
           
           if (barraPraComentarioNested != True):
               if (achouAspasNested != True):
                   contarLetrasNested = 0
                   contarAspas        = 0
                   naoEhNested        = None
                   concatenarPalavras = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagNested == True) and (achouArrobaNested == True)):
                               if (letra == "@"):
                                   if ((naoEhNested == True) and (contarLetrasNested == 7)):
                                       if ('@Nested' == concatenarPalavras):
                                           achouAbreChaveNested = False
                                           achouNested          = True
                                           naoEhNested          = False
                                           contNested           += 1
                                           contarLetrasNested   = 1
                                           concatenarPalavras   = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasNested = 1
                                       achouArrobaNested  = True
                                       concatenarPalavras = ""
                                       
                                   contarLetrasNested = 1
                                   concatenarPalavras += letra
                                   
                               elif (achouArrobaNested == True):
                                     if (contarLetrasNested == 7):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@Nested' == concatenarPalavras):
                                                 achouAbreChaveNested = False
                                                 achouNested          = True
                                                 naoEhNested          = False
                                                 contNested           += 1
                                                 contarLetrasNested   = 0
                                                 concatenarPalavras   = ""
                                             if (letra == "("):
                                                 concatenarPalavras = ""
                                                 flagNested         = False
                                                 achouArrobaNested  = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                         
                                             contarLetrasNested += 1
                                             naoEhNested        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras = ""
                                             flagNested         = False
                                             achouArrobaNested  = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasNested = 0
                                             
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasNested += 1
                                             naoEhNested        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasNested = True
                                   contarAspas      += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas      -= 2
                                   achouAspasNested = False
                                   
                               if (achouAspasNested != True):
                                   if (letra == ")"):
                                       flagNested        = True 
                                       achouArrobaNested = True
                                   elif (letra == "@"):
                                         concatenarPalavras = ""
                                         concatenarPalavras += letra
                                         contarLetrasNested = 1
                                         flagNested         = True
                                         achouArrobaNested  = True
                                     
                       else:
                           if ((naoEhNested == True) and (contarLetrasNested == 7)):
                               if ('@Nested' == concatenarPalavras):
                                   concatenarPalavras       = ""
                                   achouAbreChaveNested     = False
                                   achouNested              = True
                                   naoEhNested              = False
                                   contNested               += 1
                                   contarLetrasNested       = 0
                                   barraPraComentarioNested = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @Nested
                   if (barraPraComentarioNested != True):
                       if ((len("@Nested") == contarLetrasNested) or (len("@Nested") == contarLetrasNested - 1)):
                           if ('@Nested' == concatenarPalavras):
                               concatenarPalavras   = ""
                               contarLetrasNested   = 0
                               achouAbreChaveNested = False
                               achouNested          = True
                               contNested           += 1
             
       achouArrobaNested        = False
       achouAspasNested         = False
       barraPraComentarioNested = False
   
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@Tag' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioTag = True
               elif (letra == '"'):
                     achouAspasTag = True
               elif (letra == "@"):
                     flagTag        = True
                     achouArrobaTag = True
                     break
           
           if (barraPraComentarioTag != True):
               if (achouAspasTag != True):
                   contarLetrasTag    = 0
                   contarAspas        = 0
                   naoEhTag           = None
                   concatenarPalavras = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagTag == True) and (achouArrobaTag == True)):
                               if (letra == "@"):
                                   if ((naoEhTag == True) and (contarLetrasTag == 4)):
                                       if ('@Tag' == concatenarPalavras):
                                           achouAbreChaveTag  = False
                                           achouTag           = True
                                           naoEhTag           = False
                                           contTag            += 1
                                           contarLetrasTag    = 1
                                           concatenarPalavras = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasTag    = 1
                                       achouArrobaTag     = True
                                       concatenarPalavras = ""
                                       
                                   contarLetrasTag    = 1
                                   concatenarPalavras += letra
                                   
                               elif (achouArrobaTag == True):
                                     if (contarLetrasTag == 4):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@Tag' == concatenarPalavras):
                                                 achouAbreChaveTag  = False
                                                 achouTag           = True
                                                 naoEhTag           = False
                                                 contTag            += 1
                                                 contarLetrasTag    = 0
                                                 concatenarPalavras = ""
                                             if (letra == "("):
                                                 concatenarPalavras = ""
                                                 flagTag            = False
                                                 achouArrobaTag     = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                         
                                             contarLetrasTag += 1
                                             naoEhTag        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras = ""
                                             flagTag            = False
                                             achouArrobaTag     = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasTag = 0
                                                 
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasTag += 1
                                             naoEhTag        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasTag = True
                                   contarAspas   += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas   -= 2
                                   achouAspasTag = False
                                   
                               if (achouAspasTag != True):
                                   if (letra == ")"):
                                       flagTag        = True 
                                       achouArrobaTag = True
                                   elif (letra == "@"):
                                         concatenarPalavras = ""
                                         concatenarPalavras += letra
                                         contarLetrasTag    = 1
                                         flagTag            = True
                                         achouArrobaTag     = True
                                     
                       else:
                           if ((naoEhTag == True) and (contarLetrasTag == 4)):
                               if ('@Tag' == concatenarPalavras):
                                   concatenarPalavras    = ""
                                   achouAbreChaveTag     = False
                                   achouTag              = True
                                   naoEhTag              = False
                                   contTag               += 1
                                   contarLetrasTag       = 0
                                   barraPraComentarioTag = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @Tag
                   if (barraPraComentarioTag != True):
                       if ((len("@Tag") == contarLetrasTag) or (len("@Tag") == (contarLetrasTag - 1))):
                           if ('@Tag' == concatenarPalavras):
                               concatenarPalavras = ""
                               contarLetrasTag    = 0
                               achouAbreChaveTag  = False
                               achouTag           = True
                               contTag            += 1
             
       achouArrobaTag        = False
       achouAspasTag         = False
       barraPraComentarioTag = False 
       
   datafile = open(f, errors="ignore")   
   for line in datafile:       
       if '@Disabled' in line:
           tamanho = (len(line) - 1)
           for letra in line:
               if (letra == "/"):
                   barraPraComentarioDisabled = True
               elif (letra == "@"):
                     break
                     
           if '@DisabledOnJre' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioDisabledOnJre = True
                   elif (letra == "@"):
                         break
                         
           if '@DisabledIfSystemProperty' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioDisabledIfSystemProperty = True
                   elif (letra == "@"):
                         break
                         
           if '@DisabledIfEnvironmentVariable' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioDisabledIfEnvironmentVariable = True
                   elif (letra == "@"):
                         break
                       
           if '@DisabledIf' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioDisabledIf = True
                   elif (letra == "@"):
                         break
                         
           if '@DisabledOnOs' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioDisabledOnOs = True
                   elif (letra == "@"):
                         break
                                       
           if ((barraPraComentarioDisabled != barraPraComentarioDisabledOnJre)                 and
              (barraPraComentarioDisabled  != barraPraComentarioDisabledIfSystemProperty)      and
              (barraPraComentarioDisabled  != barraPraComentarioDisabledIfEnvironmentVariable) and
              (barraPraComentarioDisabled  != barraPraComentarioDisabledIf)                    and
              (barraPraComentarioDisabled  != barraPraComentarioDisabledOnOs)):
               for letra in line:
                   if (letra == "/"):
                       contarComentarioDisabled += 1
                   elif (letra == " ") or (letra == "	"):
                         contarComentarioDisabled += 1
                   else:
                       if (contarLetrasDisabled <= 9):
                           contarLetrasDisabled += 1
                       else:
                           contarComentarioDisabled += 1

           if (len("@Disabled") != (tamanho - (contarComentarioDisabled - 1)) and (barraPraComentarioDisabled == False)):
               for letra in line:
                   if ((letra == " ")or(letra == "	")):
                       contarAssinaturaDisabled += 1
                   elif (letra == "/"):
                         contarAssinaturaDisabled += 1
        
               for letra in line:
                   if (letra == "/"):
                       achouBarraDisabled = True
                   elif (achouBarraDisabled == True):
                         if ((letra != " ")and(letra != "	")):
                             contarAssinaturaDisabled += 1
                             decrementaDisabled       = True 
                             
               if (decrementaDisabled == True):
                   if (len("@Disabled") == (tamanho - (contarAssinaturaDisabled - 1))):
                       achouAbreChaveDisabled = False
                       achouDisabled          = True
                       contDisabled           += 1
               else:
                   if (len("@Disabled") == (tamanho - contarAssinaturaDisabled)):
                       achouAbreChaveDisabled = False
                       achouDisabled          = True
                       contDisabled           += 1
                       
               if (achouDisabled != True):
                   contarLetrasDisabled = 0
                   contarAspas          = 0
                   naoEhDisabled        = None
                   concatenarPalavras   = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagDisabled == True) and (achouArrobaDisabled == True)):
                               if (letra == "@"):
                                   if ((naoEhDisabled == True) and (contarLetrasDisabled == 9)):
                                       if ('@Disabled' == concatenarPalavras):
                                           achouAbreChaveDisabled = False
                                           achouDisabled          = True
                                           naoEhDisabled          = False
                                           contDisabled           += 1
                                           contarLetrasDisabled   = 1
                                           concatenarPalavras     = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasDisabled = 1
                                       achouArrobaDisabled  = True
                                       concatenarPalavras   = ""
                                   
                                   contarLetrasDisabled = 1
                                   concatenarPalavras   += letra
                                   
                               elif (achouArrobaDisabled == True):
                                     if (contarLetrasDisabled == 9):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@Disabled' == concatenarPalavras):
                                                 achouAbreChaveDisabled = False
                                                 achouDisabled          = True
                                                 naoEhDisabled          = False
                                                 contDisabled           += 1
                                                 contarLetrasDisabled   = 0
                                                 concatenarPalavras     = ""
                                             if (letra == "("):
                                                 concatenarPalavras  = ""
                                                 flagDisabled        = False
                                                 achouArrobaDisabled = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasDisabled += 1
                                             naoEhDisabled        = False
                                             
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras  = ""
                                             flagDisabled        = False
                                             achouArrobaDisabled = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasDisabled = 0
                                             
                                             if ((letra != " ")and(letra != "   ")):                                             
                                                 concatenarPalavras += letra
                                             
                                             contarLetrasDisabled += 1
                                             naoEhDisabled        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasDisabled = True
                                   contarAspas        += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas        -= 2
                                   achouAspasDisabled = False
                                   
                               if (achouAspasDisabled != True):
                                   if (letra == ")"):
                                       flagDisabled        = True 
                                       achouArrobaDisabled = True
                                   elif (letra == "@"):
                                         concatenarPalavras   = ""
                                         concatenarPalavras   += letra
                                         contarLetrasDisabled = 1
                                         flagDisabled         = True
                                         achouArrobaDisabled  = True
                                     
                       else:
                           if ((naoEhDisabled == True) and (contarLetrasDisabled == 9)):
                               if ('@Disabled' == concatenarPalavras):
                                   concatenarPalavras         = ""
                                   achouAbreChaveDisabled     = False
                                   achouDisabled              = True
                                   naoEhDisabled              = False
                                   contDisabled               += 1
                                   contarLetrasDisabled       = 0
                                   barraPraComentarioDisabled = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @Disabled
                   if (barraPraComentarioDisabled != True):
                       if ((len("@Disabled") == contarLetrasDisabled) or (len("@Disabled") == contarLetrasDisabled - 1)):
                           if ('@Disabled' == concatenarPalavras):
                               concatenarPalavras     = ""
                               contarLetrasDisabled   = 0
                               achouAbreChaveDisabled = False
                               achouDisabled          = True
                               contDisabled           += 1
       
       #Inicializando os valores
       contarAssinaturaDisabled = 0
       achouBarraDisabled       = False
       achouArrobaDisabled      = False
       achouAspasDisabled       = False
       decrementaDisabled       = False
       
       achouDisabled = False
       
       contarComentarioDisabled = 0
       contarLetrasDisabled     = 1        
       barraPraComentarioDisabled                      = False
       barraPraComentarioDisabledOnJre                 = False
       barraPraComentarioDisabledIfSystemProperty      = False
       barraPraComentarioDisabledIfEnvironmentVariable = False
       barraPraComentarioDisabledIf                    = False
       barraPraComentarioDisabledOnOs                  = False
   
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@Timeout' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioTimeout = True
               elif (letra == '"'):
                     achouAspasTimeout = True
               elif (letra == "@"):
                     flagTimeout        = True
                     achouArrobaTimeout = True
                     break
           
           if (barraPraComentarioTimeout != True):
               if (achouAspasTimeout != True):
                   contarLetrasTimeout = 0
                   contarAspas         = 0
                   naoEhTimeout        = None
                   concatenarPalavras  = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagTimeout == True) and (achouArrobaTimeout == True)):
                               if (letra == "@"):
                                   if ((naoEhTimeout == True) and (contarLetrasTimeout == 8)):
                                       if ('@Timeout' == concatenarPalavras):
                                           achouAbreChaveTimeout = False
                                           achouTimeout          = True
                                           naoEhTimeout          = False
                                           contTimeout           += 1
                                           contarLetrasTimeout   = 1
                                           concatenarPalavras    = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasTimeout = 1
                                       achouArrobaTimeout  = True
                                       concatenarPalavras  = ""
                                       
                                   contarLetrasTimeout = 1
                                   concatenarPalavras  += letra
                                   
                               elif (achouArrobaTimeout == True):
                                     if (contarLetrasTimeout == 8):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@Timeout' == concatenarPalavras):
                                                 achouAbreChaveTimeout = False
                                                 achouTimeout          = True
                                                 naoEhTimeout          = False
                                                 contTimeout           += 1
                                                 contarLetrasTimeout   = 0
                                                 concatenarPalavras    = ""
                                             if (letra == "("):
                                                 concatenarPalavras = ""
                                                 flagTimeout        = False
                                                 achouArrobaTimeout = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                         
                                             contarLetrasTimeout += 1
                                             naoEhTimeout        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras = ""
                                             flagTimeout        = False
                                             achouArrobaTimeout = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasTimeout = 0
                                                 
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasTimeout += 1
                                             naoEhTimeout        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasTimeout = True
                                   contarAspas       += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas       -= 2
                                   achouAspasTimeout = False
                                   
                               if (achouAspasTimeout != True):
                                   if (letra == ")"):
                                       flagTimeout        = True 
                                       achouArrobaTimeout = True
                                   elif (letra == "@"):
                                         concatenarPalavras  = ""
                                         concatenarPalavras  += letra
                                         contarLetrasTimeout = 1
                                         flagTimeout         = True
                                         achouArrobaTimeout  = True
                                     
                       else:
                           if ((naoEhTimeout == True) and (contarLetrasTimeout == 8)):
                               if ('@Timeout' == concatenarPalavras):
                                   concatenarPalavras        = ""
                                   achouAbreChaveTimeout     = False
                                   achouTimeout              = True
                                   naoEhTimeout              = False
                                   contTimeout               += 1
                                   contarLetrasTimeout       = 0
                                   barraPraComentarioTimeout = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @Timeout
                   if (barraPraComentarioTimeout != True):
                       if ((len("@Timeout") == contarLetrasTimeout) or (len("@Timeout") == contarLetrasTimeout - 1)):
                           if ('@Timeout' == concatenarPalavras):
                               concatenarPalavras    = ""
                               contarLetrasTimeout   = 0
                               achouAbreChaveTimeout = False
                               achouTimeout          = True
                               contTimeout           += 1
             
       achouArrobaTimeout        = False
       achouAspasTimeout         = False
       barraPraComentarioTimeout = False
       
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@ExtendWith' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioExtendWith = True
               elif (letra == '"'):
                     achouAspasExtendWith = True
               elif (letra == "@"):
                     flagExtendWith        = True
                     achouArrobaExtendWith = True
                     break
           
           if (barraPraComentarioExtendWith != True):
               if (achouAspasExtendWith != True):
                   contarLetrasExtendWith = 0
                   contarAspas            = 0
                   naoEhExtendWith        = None
                   concatenarPalavras     = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagExtendWith == True) and (achouArrobaExtendWith == True)):
                               if (letra == "@"):
                                   if ((naoEhExtendWith == True) and (contarLetrasExtendWith == 11)):
                                       if ('@ExtendWith' == concatenarPalavras):
                                           achouAbreChaveExtendWith = False
                                           achouExtendWith          = True
                                           naoEhExtendWith          = False
                                           contExtendWith           += 1
                                           contarLetrasExtendWith   = 1
                                           concatenarPalavras       = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasExtendWith = 1
                                       achouArrobaExtendWith  = True
                                       concatenarPalavras     = ""
                                       
                                   contarLetrasExtendWith = 1
                                   concatenarPalavras     += letra
                                   
                               elif (achouArrobaExtendWith == True):
                                     if (contarLetrasExtendWith == 11):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@ExtendWith' == concatenarPalavras):
                                                 achouAbreChaveExtendWith = False
                                                 achouExtendWith          = True
                                                 naoEhExtendWith          = False
                                                 contExtendWith           += 1
                                                 contarLetrasExtendWith   = 0
                                                 concatenarPalavras       = ""
                                             if (letra == "("):
                                                 concatenarPalavras    = ""
                                                 flagExtendWith        = False
                                                 achouArrobaExtendWith = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                          
                                             contarLetrasExtendWith += 1
                                             naoEhExtendWith        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras    = ""
                                             flagExtendWith        = False
                                             achouArrobaExtendWith = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasExtendWith = 0
                                                 
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasExtendWith += 1
                                             naoEhExtendWith        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasExtendWith = True
                                   contarAspas          += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas          -= 2
                                   achouAspasExtendWith = False
                                   
                               if (achouAspasExtendWith != True):
                                   if (letra == ")"):
                                       flagExtendWith        = True 
                                       achouArrobaExtendWith = True
                                   elif (letra == "@"):
                                         concatenarPalavras     = ""
                                         concatenarPalavras     += letra
                                         contarLetrasExtendWith = 1
                                         flagExtendWith         = True
                                         achouArrobaExtendWith  = True
                                     
                       else:
                           if ((naoEhExtendWith == True) and (contarLetrasExtendWith == 11)):
                               if ('@ExtendWith' == concatenarPalavras):
                                   concatenarPalavras           = ""
                                   achouAbreChaveExtendWith     = False
                                   achouExtendWith              = True
                                   naoEhExtendWith              = False
                                   contExtendWith               += 1
                                   contarLetrasExtendWith       = 0
                                   barraPraComentarioExtendWith = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @ExtendWith
                   if (barraPraComentarioExtendWith != True):
                       if ((len("@ExtendWith") == contarLetrasExtendWith) or (len("@ExtendWith") == contarLetrasExtendWith - 1)):
                           if ('@ExtendWith' == concatenarPalavras):
                               concatenarPalavras       = ""
                               contarLetrasExtendWith   = 0
                               achouAbreChaveExtendWith = False
                               achouExtendWith          = True
                               contExtendWith           += 1
             
       achouArrobaExtendWith        = False
       achouAspasExtendWith         = False
       barraPraComentarioExtendWith = False

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@RegisterExtension' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioRegisterExtension = True
               elif (letra == '"'):
                     achouAspasRegisterExtension = True
               elif (letra == "@"):
                     flagRegisterExtension        = True
                     achouArrobaRegisterExtension = True
                     break
           
           if (barraPraComentarioRegisterExtension != True):
               if (achouAspasRegisterExtension != True):
                   contarLetrasRegisterExtension = 0
                   contarAspas                   = 0
                   naoEhRegisterExtension        = None
                   concatenarPalavras            = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagRegisterExtension == True) and (achouArrobaRegisterExtension == True)):
                               if (letra == "@"):
                                   if ((naoEhRegisterExtension == True) and (contarLetrasRegisterExtension == 18)):
                                       if ('@RegisterExtension' == concatenarPalavras):
                                           achouAbreChaveRegisterExtension = False
                                           achouRegisterExtension          = True
                                           naoEhRegisterExtension          = False
                                           contRegisterExtension           += 1
                                           contarLetrasRegisterExtension   = 1
                                           concatenarPalavras              = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasRegisterExtension = 1
                                       achouArrobaRegisterExtension  = True
                                       concatenarPalavras            = ""
                                       
                                   contarLetrasRegisterExtension = 1
                                   concatenarPalavras            += letra
                                   
                               elif (achouArrobaRegisterExtension == True):
                                     if (contarLetrasRegisterExtension == 18):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@RegisterExtension' == concatenarPalavras):
                                                 achouAbreChaveRegisterExtension = False
                                                 achouRegisterExtension          = True
                                                 naoEhRegisterExtension          = False
                                                 contRegisterExtension           += 1
                                                 contarLetrasRegisterExtension   = 0
                                                 concatenarPalavras              = ""
                                             if (letra == "("):
                                                 concatenarPalavras           = ""
                                                 flagRegisterExtension        = False
                                                 achouArrobaRegisterExtension = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasRegisterExtension += 1
                                             naoEhRegisterExtension        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras           = ""
                                             flagRegisterExtension        = False
                                             achouArrobaRegisterExtension = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasRegisterExtension = 0
                                                 
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasRegisterExtension += 1
                                             naoEhRegisterExtension        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasRegisterExtension = True
                                   contarAspas                 += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas                 -= 2
                                   achouAspasRegisterExtension = False
                                   
                               if (achouAspasRegisterExtension != True):
                                   if (letra == ")"):
                                       flagRegisterExtension        = True 
                                       achouArrobaRegisterExtension = True
                                   elif (letra == "@"):
                                         concatenarPalavras            = ""
                                         concatenarPalavras            += letra
                                         contarLetrasRegisterExtension = 1
                                         flagRegisterExtension         = True
                                         achouArrobaRegisterExtension  = True
                                     
                       else:
                           if ((naoEhRegisterExtension == True) and (contarLetrasRegisterExtension == 18)):
                               if ('@RegisterExtension' == concatenarPalavras):
                                   concatenarPalavras                  = ""
                                   achouAbreChaveRegisterExtension     = False
                                   achouRegisterExtension              = True
                                   naoEhRegisterExtension              = False
                                   contRegisterExtension               += 1
                                   contarLetrasRegisterExtension       = 0
                                   barraPraComentarioRegisterExtension = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @RegisterExtension
                   if (barraPraComentarioRegisterExtension != True):
                       if ((len("@RegisterExtension") == contarLetrasRegisterExtension) or (len("@RegisterExtension") == contarLetrasRegisterExtension - 1)):
                           if ('@RegisterExtension' == concatenarPalavras):
                               concatenarPalavras              = ""
                               contarLetrasRegisterExtension   = 0
                               achouAbreChaveRegisterExtension = False
                               achouRegisterExtension          = True
                               contRegisterExtension           += 1
             
       achouArrobaRegisterExtension        = False
       achouAspasRegisterExtension         = False
       barraPraComentarioRegisterExtension = False

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@TempDir' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioTempDir = True
               elif (letra == '"'):
                     achouAspasTempDir = True
               elif (letra == "@"):
                     flagTempDir        = True
                     achouArrobaTempDir = True
                     break
           
           if (barraPraComentarioTempDir != True):
               if (achouAspasTempDir != True):
                   contarLetrasTempDir = 0
                   contarAspas         = 0
                   naoEhTempDir        = None
                   concatenarPalavras  = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagTempDir == True) and (achouArrobaTempDir == True)):
                               if (letra == "@"):
                                   if ((naoEhTempDir == True) and (contarLetrasTempDir == 8)):
                                       if ('@TempDir' == concatenarPalavras):
                                           achouAbreChaveTempDir = False
                                           achouTempDir          = True
                                           naoEhTempDir          = False
                                           contTempDir           += 1
                                           contarLetrasTempDir   = 1
                                           concatenarPalavras    = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasTempDir = 1
                                       achouArrobaTempDir  = True
                                       concatenarPalavras  = ""
                                   
                                   contarLetrasTempDir = 1
                                   concatenarPalavras  += letra
                                   
                               elif (achouArrobaTempDir == True):
                                     if (contarLetrasTempDir == 8):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@TempDir' == concatenarPalavras):
                                                 achouAbreChaveTempDir = False
                                                 achouTempDir          = True
                                                 naoEhTempDir          = False
                                                 contTempDir           += 1
                                                 contarLetrasTempDir   = 0
                                                 concatenarPalavras    = ""
                                             if (letra == "("):
                                                 concatenarPalavras = ""
                                                 flagTempDir        = False
                                                 achouArrobaTempDir = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasTempDir += 1
                                             naoEhTempDir        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras = ""
                                             flagTempDir        = False
                                             achouArrobaTempDir = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasTempDir = 0
                                                 
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasTempDir += 1
                                             naoEhTempDir        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasTempDir = True
                                   contarAspas       += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas       -= 2
                                   achouAspasTempDir = False
                                   
                               if (achouAspasTempDir != True):
                                   if (letra == ")"):
                                       flagTempDir        = True 
                                       achouArrobaTempDir = True
                                   elif (letra == "@"):
                                         concatenarPalavras  = ""
                                         concatenarPalavras  += letra
                                         contarLetrasTempDir = 1
                                         flagTempDir         = True
                                         achouArrobaTempDir  = True
                                     
                       else:
                           if ((naoEhTempDir == True) and (contarLetrasTempDir == 8)):
                               if ('@TempDir' == concatenarPalavras):
                                   concatenarPalavras        = ""
                                   achouAbreChaveTempDir     = False
                                   achouTempDir              = True
                                   naoEhTempDir              = False
                                   contTempDir               += 1
                                   contarLetrasTempDir       = 0
                                   barraPraComentarioTempDir = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @TempDir
                   if (barraPraComentarioTempDir != True):
                       if ((len("@TempDir") == contarLetrasTempDir) or (len("@TempDir") == contarLetrasTempDir - 1)):
                           if ('@TempDir' == concatenarPalavras):
                               concatenarPalavras    = ""
                               contarLetrasTempDir   = 0
                               achouAbreChaveTempDir = False
                               achouTempDir          = True
                               contTempDir           += 1
             
       achouArrobaTempDir        = False
       achouAspasTempDir         = False
       barraPraComentarioTempDir = False

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@TestOnMac' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioTestOnMac = True
               elif (letra == '"'):
                     achouAspasTestOnMac = True
               elif (letra == "@"):
                     flagTestOnMac        = True
                     achouArrobaTestOnMac = True
                     break
           
           if (barraPraComentarioTestOnMac != True):
               if (achouAspasTestOnMac != True):
                   contarLetrasTestOnMac = 0
                   contarAspas           = 0
                   naoEhTestOnMac        = None
                   concatenarPalavras    = ""
                   
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagTestOnMac == True) and (achouArrobaTestOnMac == True)):
                               if (letra == "@"):
                                   if ((naoEhTestOnMac == True) and (contarLetrasTestOnMac == 10)):
                                       if ('@TestOnMac' == concatenarPalavras):
                                           achouAbreChaveTestOnMac = False
                                           achouTestOnMac          = True
                                           naoEhTestOnMac          = False
                                           contTestOnMac           += 1
                                           contarLetrasTestOnMac   = 1
                                           concatenarPalavras      = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasTestOnMac = 1
                                       achouArrobaTestOnMac  = True
                                       concatenarPalavras    = ""
                                       
                                   contarLetrasTestOnMac = 1
                                   concatenarPalavras    += letra
                                   
                               elif (achouArrobaTestOnMac == True):
                                     if (contarLetrasTestOnMac == 10):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@TestOnMac' == concatenarPalavras):
                                                 achouAbreChaveTestOnMac = False
                                                 achouTestOnMac          = True
                                                 naoEhTestOnMac          = False
                                                 contTestOnMac           += 1
                                                 contarLetrasTestOnMac   = 0
                                                 concatenarPalavras      = ""
                                             if (letra == "("):
                                                 concatenarPalavras   = ""
                                                 flagTestOnMac        = False
                                                 achouArrobaTestOnMac = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasTestOnMac += 1
                                             naoEhTestOnMac        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras   = ""
                                             flagTestOnMac        = False
                                             achouArrobaTestOnMac = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasTestOnMac = 0
                                             
                                             if ((letra != " ")and(letra != "	")):                                             
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasTestOnMac += 1
                                             naoEhTestOnMac        = True
                                             
                           else:             
                               if (letra == '"'):
                                   achouAspasTestOnMac = True
                                   contarAspas         += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas         -= 2
                                   achouAspasTestOnMac = False
                                   
                               if (achouAspasTestOnMac != True):
                                   if (letra == ")"):
                                       flagTestOnMac        = True 
                                       achouArrobaTestOnMac = True
                                   elif (letra == "@"):
                                         concatenarPalavras    = ""
                                         concatenarPalavras    += letra
                                         contarLetrasTestOnMac = 1
                                         flagTestOnMac         = True
                                         achouArrobaTestOnMac  = True
                                     
                       else:
                           if ((naoEhTestOnMac == True) and (contarLetrasTestOnMac == 10)):
                               if ('@TestOnMac' == concatenarPalavras):
                                   concatenarPalavras          = ""
                                   achouAbreChaveTestOnMac     = False
                                   achouTestOnMac              = True
                                   naoEhTestOnMac              = False
                                   contTestOnMac               += 1
                                   contarLetrasTestOnMac       = 0
                                   barraPraComentarioTestOnMac = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @TestOnMac
                   if (barraPraComentarioTestOnMac != True):
                       if ((len("@TestOnMac") == contarLetrasTestOnMac) or (len("@TestOnMac") == contarLetrasTestOnMac - 1)):
                           if ('@TestOnMac' == concatenarPalavras):
                               concatenarPalavras      = ""
                               contarLetrasTestOnMac   = 0
                               achouAbreChaveTestOnMac = False
                               achouTestOnMac          = True
                               contTestOnMac           += 1
             
       achouArrobaTestOnMac        = False
       achouAspasTestOnMac         = False
       barraPraComentarioTestOnMac = False 
 
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@Order' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioOrder = True
               elif (letra == '"'):
                     achouAspasOrder = True
               elif (letra == "@"):
                     flagOrder        = True
                     achouArrobaOrder = True
                     break
           
           if (barraPraComentarioOrder != True):
               if (achouAspasOrder != True):
                   contarLetrasOrder  = 0
                   contarAspas        = 0
                   naoEhOrder         = None
                   concatenarPalavras = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagOrder == True) and (achouArrobaOrder == True)):
                               if (letra == "@"):
                                   if ((naoEhOrder == True) and (contarLetrasOrder == 6)):
                                       if ('@Order' == concatenarPalavras):
                                           achouAbreChaveOrder = False
                                           achouOrder          = True
                                           naoEhOrder          = False
                                           contOrder           += 1
                                           contarLetrasOrder   = 1
                                           concatenarPalavras  = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasOrder  = 1
                                       achouArrobaOrder   = True
                                       concatenarPalavras = ""
                                       
                                   contarLetrasOrder  = 1
                                   concatenarPalavras += letra
                                   
                               elif (achouArrobaOrder == True):
                                     if (contarLetrasOrder == 6):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@Order' == concatenarPalavras):
                                                 achouAbreChaveOrder = False
                                                 achouOrder          = True
                                                 naoEhOrder          = False
                                                 contOrder           += 1
                                                 contarLetrasOrder   = 0
                                                 concatenarPalavras  = ""
                                             if (letra == "("):
                                                 concatenarPalavras = ""
                                                 flagOrder          = False
                                                 achouArrobaOrder   = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasOrder += 1
                                             naoEhOrder        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras = ""
                                             flagOrder          = False
                                             achouArrobaOrder   = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasOrder = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasOrder += 1
                                             naoEhOrder        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasOrder = True
                                   contarAspas     += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas     -= 2
                                   achouAspasOrder = False
                                   
                               if (achouAspasOrder != True):
                                   if (letra == ")"):
                                       flagOrder        = True 
                                       achouArrobaOrder = True
                                   elif (letra == "@"):
                                         concatenarPalavras = ""
                                         concatenarPalavras += letra
                                         contarLetrasOrder  = 1
                                         flagOrder          = True
                                         achouArrobaOrder   = True
                                     
                       else:
                           if ((naoEhOrder == True) and (contarLetrasOrder == 6)):
                               if ('@Order' == concatenarPalavras):
                                   concatenarPalavras      = ""
                                   achouAbreChaveOrder     = False
                                   achouOrder              = True
                                   naoEhOrder              = False
                                   contOrder               += 1
                                   contarLetrasOrder       = 0
                                   barraPraComentarioOrder = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @Order
                   if (barraPraComentarioOrder != True):
                       if ((len("@Order") == contarLetrasOrder) or (len("@Order") == contarLetrasOrder - 1)):
                           if ('@Order' == concatenarPalavras):
                               concatenarPalavras  = ""
                               contarLetrasOrder   = 0
                               achouAbreChaveOrder = False
                               achouOrder          = True
                               contOrder           += 1
             
       achouArrobaOrder        = False
       achouAspasOrder         = False
       barraPraComentarioOrder = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@Target' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioTarget = True
               elif (letra == '"'):
                     achouAspasTarget = True
               elif (letra == "@"):
                     flagTarget        = True
                     achouArrobaTarget = True
                     break
           
           if (barraPraComentarioTarget != True):
               if (achouAspasTarget != True):
                   contarLetrasTarget = 0
                   contarAspas        = 0
                   naoEhTarget        = None
                   concatenarPalavras = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagTarget == True) and (achouArrobaTarget == True)):
                               if (letra == "@"):
                                   if ((naoEhTarget == True) and (contarLetrasTarget == 7)):
                                       if ('@Target' == concatenarPalavras):
                                           achouAbreChaveTarget = False
                                           achouTarget          = True
                                           naoEhTarget          = False
                                           contTarget           += 1
                                           contarLetrasTarget   = 1
                                           concatenarPalavras   = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasTarget = 1
                                       achouArrobaTarget  = True
                                       concatenarPalavras = ""
                                   
                                   contarLetrasTarget = 1
                                   concatenarPalavras += letra
                                   
                               elif (achouArrobaTarget == True):
                                     if (contarLetrasTarget == 7):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@Target' == concatenarPalavras):
                                                 achouAbreChaveTarget = False
                                                 achouTarget          = True
                                                 naoEhTarget          = False
                                                 contTarget           += 1
                                                 contarLetrasTarget   = 0
                                                 concatenarPalavras   = ""
                                             if (letra == "("):
                                                 concatenarPalavras = ""
                                                 flagTarget         = False
                                                 achouArrobaTarget  = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasTarget += 1
                                             naoEhTarget        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras = ""
                                             flagTarget         = False
                                             achouArrobaTarget  = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasTarget = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasTarget += 1
                                             naoEhTarget        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasTarget = True
                                   contarAspas      += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas      -= 2
                                   achouAspasTarget = False
                                   
                               if (achouAspasTarget != True):
                                   if (letra == ")"):
                                       flagTarget        = True 
                                       achouArrobaTarget = True
                                   elif (letra == "@"):
                                         concatenarPalavras = ""
                                         concatenarPalavras += letra
                                         contarLetrasTarget = 1
                                         flagTarget         = True
                                         achouArrobaTarget  = True
                                     
                       else:
                           if ((naoEhTarget == True) and (contarLetrasTarget == 7)):
                               if ('@Target' == concatenarPalavras):
                                   concatenarPalavras       = ""
                                   achouAbreChaveTarget     = False
                                   achouTarget              = True
                                   naoEhTarget              = False
                                   contTarget               += 1
                                   contarLetrasTarget       = 0
                                   barraPraComentarioTarget = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @Target
                   if (barraPraComentarioTarget != True):
                       if ((len("@Target") == contarLetrasTarget) or (len("@Target") == contarLetrasTarget - 1)):
                           if ('@Target' == concatenarPalavras):
                               concatenarPalavras   = ""
                               contarLetrasTarget   = 0
                               achouAbreChaveTarget = False
                               achouTarget          = True
                               contTarget           += 1
             
       achouArrobaTarget        = False
       achouAspasTarget         = False
       barraPraComentarioTarget = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@Retention' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioRetention = True
               elif (letra == '"'):
                     achouAspasRetention = True
               elif (letra == "@"):
                     flagRetention        = True
                     achouArrobaRetention = True
                     break
           
           if (barraPraComentarioRetention != True):
               if (achouAspasRetention != True):
                   contarLetrasRetention = 0
                   contarAspas           = 0
                   naoEhRetention        = None
                   concatenarPalavras    = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagRetention == True) and (achouArrobaRetention == True)):
                               if (letra == "@"):
                                   if ((naoEhRetention == True) and (contarLetrasRetention == 10)):
                                       if ('@Retention' == concatenarPalavras):
                                           achouAbreChaveRetention = False
                                           achouRetention          = True
                                           naoEhRetention          = False
                                           contRetention           += 1
                                           contarLetrasRetention   = 1
                                           concatenarPalavras      = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasRetention = 1
                                       achouArrobaRetention  = True
                                       concatenarPalavras    = ""
                                       
                                   contarLetrasRetention = 1
                                   concatenarPalavras    += letra
                                   
                               elif (achouArrobaRetention == True):
                                     if (contarLetrasRetention == 10):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@Retention' == concatenarPalavras):
                                                 achouAbreChaveRetention = False
                                                 achouRetention          = True
                                                 naoEhRetention          = False
                                                 contRetention           += 1
                                                 contarLetrasRetention   = 0
                                                 concatenarPalavras      = ""
                                             if (letra == "("):
                                                 concatenarPalavras   = ""
                                                 flagRetention        = False
                                                 achouArrobaRetention = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasRetention += 1
                                             naoEhRetention        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras   = ""
                                             flagRetention        = False
                                             achouArrobaRetention = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasRetention = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasRetention += 1
                                             naoEhRetention        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasRetention = True
                                   contarAspas         += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas         -= 2
                                   achouAspasRetention = False
                                   
                               if (achouAspasRetention != True):
                                   if (letra == ")"):
                                       flagRetention        = True 
                                       achouArrobaRetention = True
                                   elif (letra == "@"):
                                         concatenarPalavras    = ""
                                         concatenarPalavras    += letra
                                         contarLetrasRetention = 1
                                         flagRetention         = True
                                         achouArrobaRetention  = True
                                     
                       else:
                           if ((naoEhRetention == True) and (contarLetrasRetention == 10)):
                               if ('@Retention' == concatenarPalavras):
                                   concatenarPalavras          = ""
                                   achouAbreChaveRetention     = False
                                   achouRetention              = True
                                   naoEhRetention              = False
                                   contRetention               += 1
                                   contarLetrasRetention       = 0
                                   barraPraComentarioRetention = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @Retention
                   if (barraPraComentarioRetention != True):
                       if ((len("@Retention") == contarLetrasRetention) or (len("@Retention") == contarLetrasRetention - 1)):
                           if ('@Retention' == concatenarPalavras):
                               concatenarPalavras      = ""
                               contarLetrasRetention   = 0
                               achouAbreChaveRetention = False
                               achouRetention          = True
                               contRetention           += 1
             
       achouArrobaRetention        = False
       achouAspasRetention         = False
       barraPraComentarioRetention = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@ValueSource' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioValueSource = True
               elif (letra == '"'):
                     achouAspasValueSource = True
               elif (letra == "@"):
                     flagValueSource        = True
                     achouArrobaValueSource = True
                     break
           
           if (barraPraComentarioValueSource != True):
               if (achouAspasValueSource != True):
                   contarLetrasValueSource = 0
                   contarAspas             = 0
                   naoEhValueSource        = None
                   concatenarPalavras      = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagValueSource == True) and (achouArrobaValueSource == True)):
                               if (letra == "@"):
                                   if ((naoEhValueSource == True) and (contarLetrasValueSource == 12)):
                                       if ('@ValueSource' == concatenarPalavras):
                                           achouAbreChaveValueSource = False
                                           achouValueSource          = True
                                           naoEhValueSource          = False
                                           contValueSource           += 1
                                           contarLetrasValueSource   = 1
                                           concatenarPalavras        = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasValueSource = 1
                                       achouArrobaValueSource  = True
                                       concatenarPalavras      = ""
                                       
                                   contarLetrasValueSource = 1
                                   concatenarPalavras      += letra
                                   
                               elif (achouArrobaValueSource == True):
                                     if (contarLetrasValueSource == 12):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@ValueSource' == concatenarPalavras):
                                                 achouAbreChaveValueSource = False
                                                 achouValueSource          = True
                                                 naoEhValueSource          = False
                                                 contValueSource           += 1
                                                 contarLetrasValueSource   = 0
                                                 concatenarPalavras        = ""
                                             if (letra == "("):
                                                 concatenarPalavras     = ""
                                                 flagValueSource        = False
                                                 achouArrobaValueSource = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasValueSource += 1
                                             naoEhValueSource        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras     = ""
                                             flagValueSource        = False
                                             achouArrobaValueSource = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasValueSource = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasValueSource += 1
                                             naoEhValueSource        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasValueSource = True
                                   contarAspas           += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas           -= 2
                                   achouAspasValueSource = False
                                   
                               if (achouAspasValueSource != True):
                                   if (letra == ")"):
                                       flagValueSource        = True 
                                       achouArrobaValueSource = True
                                   elif (letra == "@"):
                                         concatenarPalavras      = ""
                                         concatenarPalavras      += letra
                                         contarLetrasValueSource = 1
                                         flagValueSource         = True
                                         achouArrobaValueSource  = True
                                     
                       else:
                           if ((naoEhValueSource == True) and (contarLetrasValueSource == 12)):
                               if ('@ValueSource' == concatenarPalavras):
                                   concatenarPalavras            = ""
                                   achouAbreChaveValueSource     = False
                                   achouValueSource              = True
                                   naoEhValueSource              = False
                                   contValueSource               += 1
                                   contarLetrasValueSource       = 0
                                   barraPraComentarioValueSource = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @ValueSource
                   if (barraPraComentarioValueSource != True):
                       if ((len("@ValueSource") == contarLetrasValueSource) or (len("@ValueSource") == contarLetrasValueSource - 1)):
                           if ('@ValueSource' == concatenarPalavras):
                               concatenarPalavras        = ""
                               contarLetrasValueSource   = 0
                               achouAbreChaveValueSource = False
                               achouValueSource          = True
                               contValueSource           += 1

       achouArrobaValueSource        = False
       achouAspasValueSource         = False
       barraPraComentarioValueSource = False 
 
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@EnabledOnOs' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioEnabledOnOs = True
               elif (letra == '"'):
                     achouAspasEnabledOnOs = True
               elif (letra == "@"):
                     flagEnabledOnOs        = True
                     achouArrobaEnabledOnOs = True
                     break
           
           if (barraPraComentarioEnabledOnOs != True):
               if (achouAspasEnabledOnOs != True):
                   contarLetrasEnabledOnOs = 0
                   contarAspas             = 0
                   naoEhEnabledOnOs        = None
                   concatenarPalavras      = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagEnabledOnOs == True) and (achouArrobaEnabledOnOs == True)):
                               if (letra == "@"):
                                   if ((naoEhEnabledOnOs == True) and (contarLetrasEnabledOnOs == 12)):
                                       if ('@EnabledOnOs' == concatenarPalavras):
                                           achouAbreChaveEnabledOnOs = False
                                           achouEnabledOnOs          = True
                                           naoEhEnabledOnOs          = False
                                           contEnabledOnOs           += 1
                                           contarLetrasEnabledOnOs   = 1
                                           concatenarPalavras        = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasEnabledOnOs = 1
                                       achouArrobaEnabledOnOs  = True
                                       concatenarPalavras      = ""
                                       
                                   contarLetrasEnabledOnOs = 1
                                   concatenarPalavras      += letra
                                   
                               elif (achouArrobaEnabledOnOs == True):
                                     if (contarLetrasEnabledOnOs == 12):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@EnabledOnOs' == concatenarPalavras):
                                                 achouAbreChaveEnabledOnOs = False
                                                 achouEnabledOnOs          = True
                                                 naoEhEnabledOnOs          = False
                                                 contEnabledOnOs           += 1
                                                 contarLetrasEnabledOnOs   = 0
                                                 concatenarPalavras        = ""
                                             if (letra == "("):
                                                 concatenarPalavras     = ""
                                                 flagEnabledOnOs        = False
                                                 achouArrobaEnabledOnOs = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasEnabledOnOs += 1
                                             naoEhEnabledOnOs        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras     = ""
                                             flagEnabledOnOs        = False
                                             achouArrobaEnabledOnOs = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasEnabledOnOs = 0
                                             
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasEnabledOnOs += 1
                                             naoEhEnabledOnOs        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasEnabledOnOs = True
                                   contarAspas           += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas           -= 2
                                   achouAspasEnabledOnOs = False
                                   
                               if (achouAspasEnabledOnOs != True):
                                   if (letra == ")"):
                                       flagEnabledOnOs        = True 
                                       achouArrobaEnabledOnOs = True
                                   elif (letra == "@"):
                                         concatenarPalavras      = ""
                                         concatenarPalavras      += letra
                                         contarLetrasEnabledOnOs = 1
                                         flagEnabledOnOs         = True
                                         achouArrobaEnabledOnOs  = True
                                     
                       else:
                           if ((naoEhEnabledOnOs == True) and (contarLetrasEnabledOnOs == 12)):
                               if ('@EnabledOnOs' == concatenarPalavras):
                                   concatenarPalavras            = ""
                                   achouAbreChaveEnabledOnOs     = False
                                   achouEnabledOnOs              = True
                                   naoEhEnabledOnOs              = False
                                   contEnabledOnOs               += 1
                                   contarLetrasEnabledOnOs       = 0
                                   barraPraComentarioEnabledOnOs = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @EnabledOnOs
                   if (barraPraComentarioEnabledOnOs != True):
                       if ((len("@EnabledOnOs") == contarLetrasEnabledOnOs) or (len("@EnabledOnOs") == contarLetrasEnabledOnOs - 1)):
                           if ('@EnabledOnOs' == concatenarPalavras):
                               concatenarPalavras        = ""
                               contarLetrasEnabledOnOs   = 0
                               achouAbreChaveEnabledOnOs = False
                               achouEnabledOnOs          = True
                               contEnabledOnOs           += 1
             
       achouArrobaEnabledOnOs        = False
       achouAspasEnabledOnOs         = False
       barraPraComentarioEnabledOnOs = False 
   
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@DisabledOnOs' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioDisabledOnOs = True
               elif (letra == '"'):
                     achouAspasDisabledOnOs = True
               elif (letra == "@"):
                     flagDisabledOnOs        = True
                     achouArrobaDisabledOnOs = True
                     break
           
           if (barraPraComentarioDisabledOnOs != True):
               if (achouAspasDisabledOnOs != True):
                   contarLetrasDisabledOnOs = 0
                   contarAspas              = 0
                   naoEhDisabledOnOs        = None
                   concatenarPalavras       = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagDisabledOnOs == True) and (achouArrobaDisabledOnOs == True)):
                               if (letra == "@"):
                                   if ((naoEhDisabledOnOs == True) and (contarLetrasDisabledOnOs == 13)):
                                       if ('@DisabledOnOs' == concatenarPalavras):
                                           achouAbreChaveDisabledOnOs = False
                                           achouDisabledOnOs          = True
                                           naoEhDisabledOnOs          = False
                                           contDisabledOnOs           += 1
                                           contarLetrasDisabledOnOs   = 1
                                           concatenarPalavras         = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasDisabledOnOs = 1
                                       achouArrobaDisabledOnOs  = True
                                       concatenarPalavras       = ""
                                       
                                   contarLetrasDisabledOnOs = 1
                                   concatenarPalavras       += letra
                                   
                               elif (achouArrobaDisabledOnOs == True):
                                     if (contarLetrasDisabledOnOs == 13):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@DisabledOnOs' == concatenarPalavras):
                                                 achouAbreChaveDisabledOnOs = False
                                                 achouDisabledOnOs          = True
                                                 naoEhDisabledOnOs          = False
                                                 contDisabledOnOs           += 1
                                                 contarLetrasDisabledOnOs   = 0
                                                 concatenarPalavras         = ""
                                             if (letra == "("):
                                                 concatenarPalavras      = ""
                                                 flagDisabledOnOs        = False
                                                 achouArrobaDisabledOnOs = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasDisabledOnOs += 1
                                             naoEhDisabledOnOs        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras      = ""
                                             flagDisabledOnOs        = False
                                             achouArrobaDisabledOnOs = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasDisabledOnOs = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasDisabledOnOs += 1
                                             naoEhDisabledOnOs        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasDisabledOnOs = True
                                   contarAspas            += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas            -= 2
                                   achouAspasDisabledOnOs = False
                                   
                               if (achouAspasDisabledOnOs != True):
                                   if (letra == ")"):
                                       flagDisabledOnOs        = True 
                                       achouArrobaDisabledOnOs = True
                                   elif (letra == "@"):
                                         concatenarPalavras       = ""
                                         concatenarPalavras       += letra
                                         contarLetrasDisabledOnOs = 1
                                         flagDisabledOnOs         = True
                                         achouArrobaDisabledOnOs  = True
                                     
                       else:
                           if ((naoEhDisabledOnOs == True) and (contarLetrasDisabledOnOs == 13)):
                               if ('@DisabledOnOs' == concatenarPalavras):
                                   concatenarPalavras             = ""
                                   achouAbreChaveDisabledOnOs     = False
                                   achouDisabledOnOs              = True
                                   naoEhDisabledOnOs              = False
                                   contDisabledOnOs               += 1
                                   contarLetrasDisabledOnOs       = 0
                                   barraPraComentarioDisabledOnOs = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @DisabledOnOs
                   if (barraPraComentarioDisabledOnOs != True):
                       if ((len("@DisabledOnOs") == contarLetrasDisabledOnOs) or (len("@DisabledOnOs") == contarLetrasDisabledOnOs - 1)):
                           if ('@DisabledOnOs' == concatenarPalavras):
                               concatenarPalavras         = ""
                               contarLetrasDisabledOnOs   = 0
                               achouAbreChaveDisabledOnOs = False
                               achouDisabledOnOs          = True
                               contDisabledOnOs           += 1
             
       achouArrobaDisabledOnOs        = False
       achouAspasDisabledOnOs         = False
       barraPraComentarioDisabledOnOs = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@EnabledOnJre' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioEnabledOnJre = True
               elif (letra == '"'):
                     achouAspasEnabledOnJre = True
               elif (letra == "@"):
                     flagEnabledOnJre        = True
                     achouArrobaEnabledOnJre = True
                     break
           
           if (barraPraComentarioEnabledOnJre != True):
               if (achouAspasEnabledOnJre != True):
                   contarLetrasEnabledOnJre = 0
                   contarAspas              = 0
                   naoEhEnabledOnJre        = None
                   concatenarPalavras       = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagEnabledOnJre == True) and (achouArrobaEnabledOnJre == True)):
                               if (letra == "@"):
                                   if ((naoEhEnabledOnJre == True) and (contarLetrasEnabledOnJre == 13)):
                                       if ('@EnabledOnJre' == concatenarPalavras):
                                           achouAbreChaveEnabledOnJre = False
                                           achouEnabledOnJre          = True
                                           naoEhEnabledOnJre          = False
                                           contEnabledOnJre           += 1
                                           contarLetrasEnabledOnJre   = 1
                                           concatenarPalavras         = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasEnabledOnJre = 1
                                       achouArrobaEnabledOnJre  = True
                                       concatenarPalavras       = ""
                                       
                                   contarLetrasEnabledOnJre = 1
                                   concatenarPalavras       += letra
                                   
                               elif (achouArrobaEnabledOnJre == True):
                                     if (contarLetrasEnabledOnJre == 13):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@EnabledOnJre' == concatenarPalavras):
                                                 achouAbreChaveEnabledOnJre = False
                                                 achouEnabledOnJre          = True
                                                 naoEhEnabledOnJre          = False
                                                 contEnabledOnJre           += 1
                                                 contarLetrasEnabledOnJre   = 0
                                                 concatenarPalavras         = ""
                                             if (letra == "("):
                                                 concatenarPalavras      = ""
                                                 flagEnabledOnJre        = False
                                                 achouArrobaEnabledOnJre = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasEnabledOnJre += 1
                                             naoEhEnabledOnJre        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras      = ""
                                             flagEnabledOnJre        = False
                                             achouArrobaEnabledOnJre = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasEnabledOnJre = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasEnabledOnJre += 1
                                             naoEhEnabledOnJre        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasEnabledOnJre = True
                                   contarAspas            += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas            -= 2
                                   achouAspasEnabledOnJre = False
                                   
                               if (achouAspasEnabledOnJre != True):
                                   if (letra == ")"):
                                       flagEnabledOnJre        = True 
                                       achouArrobaEnabledOnJre = True
                                   elif (letra == "@"):
                                         concatenarPalavras       = ""
                                         concatenarPalavras       += letra
                                         contarLetrasEnabledOnJre = 1
                                         flagEnabledOnJre         = True
                                         achouArrobaEnabledOnJre  = True
                                     
                       else:
                           if ((naoEhEnabledOnJre == True) and (contarLetrasEnabledOnJre == 13)):
                               if ('@EnabledOnJre' == concatenarPalavras):
                                   concatenarPalavras             = ""
                                   achouAbreChaveEnabledOnJre     = False
                                   achouEnabledOnJre              = True
                                   naoEhEnabledOnJre              = False
                                   contEnabledOnJre               += 1
                                   contarLetrasEnabledOnJre       = 0
                                   barraPraComentarioEnabledOnJre = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @EnabledOnJre
                   if (barraPraComentarioEnabledOnJre != True):
                       if ((len("@EnabledOnJre") == contarLetrasEnabledOnJre) or (len("@EnabledOnJre") == contarLetrasEnabledOnJre - 1)):
                           if ('@EnabledOnJre' == concatenarPalavras):
                               concatenarPalavras         = ""
                               contarLetrasEnabledOnJre   = 0
                               achouAbreChaveEnabledOnJre = False
                               achouEnabledOnJre          = True
                               contEnabledOnJre           += 1

       achouArrobaEnabledOnJre        = False
       achouAspasEnabledOnJre         = False
       barraPraComentarioEnabledOnJre = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@DisabledOnJre' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioDisabledOnJre = True
               elif (letra == '"'):
                     achouAspasDisabledOnJre = True
               elif (letra == "@"):
                     flagDisabledOnJre        = True
                     achouArrobaDisabledOnJre = True
                     break
           
           if (barraPraComentarioDisabledOnJre != True):
               if (achouAspasDisabledOnJre != True):
                   contarLetrasDisabledOnJre = 0
                   contarAspas               = 0
                   naoEhDisabledOnJre        = None
                   concatenarPalavras        = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagDisabledOnJre == True) and (achouArrobaDisabledOnJre == True)):
                               if (letra == "@"):
                                   if ((naoEhDisabledOnJre == True) and (contarLetrasDisabledOnJre == 14)):
                                       if ('@DisabledOnJre' == concatenarPalavras):
                                           achouAbreChaveDisabledOnJre = False
                                           achouDisabledOnJre          = True
                                           naoEhDisabledOnJre          = False
                                           contDisabledOnJre           += 1
                                           contarLetrasDisabledOnJre   = 1
                                           concatenarPalavras          = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasDisabledOnJre = 1
                                       achouArrobaDisabledOnJre  = True
                                       concatenarPalavras        = ""
                                       
                                   contarLetrasDisabledOnJre = 1
                                   concatenarPalavras        += letra
                                   
                               elif (achouArrobaDisabledOnJre == True):
                                     if (contarLetrasDisabledOnJre == 14):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@DisabledOnJre' == concatenarPalavras):
                                                 achouAbreChaveDisabledOnJre = False
                                                 achouDisabledOnJre          = True
                                                 naoEhDisabledOnJre          = False
                                                 contDisabledOnJre           += 1
                                                 contarLetrasDisabledOnJre   = 0
                                                 concatenarPalavras          = ""
                                             if (letra == "("):
                                                 concatenarPalavras       = ""
                                                 flagDisabledOnJre        = False
                                                 achouArrobaDisabledOnJre = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasDisabledOnJre += 1
                                             naoEhDisabledOnJre        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras       = ""
                                             flagDisabledOnJre        = False
                                             achouArrobaDisabledOnJre = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasDisabledOnJre = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasDisabledOnJre += 1
                                             naoEhDisabledOnJre        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasDisabledOnJre = True
                                   contarAspas             += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas             -= 2
                                   achouAspasDisabledOnJre = False
                                   
                               if (achouAspasDisabledOnJre != True):
                                   if (letra == ")"):
                                       flagDisabledOnJre        = True 
                                       achouArrobaDisabledOnJre = True
                                   elif (letra == "@"):
                                         concatenarPalavras        = ""
                                         concatenarPalavras        += letra
                                         contarLetrasDisabledOnJre = 1
                                         flagDisabledOnJre         = True
                                         achouArrobaDisabledOnJre  = True
                                     
                       else:
                           if ((naoEhDisabledOnJre == True) and (contarLetrasDisabledOnJre == 14)):
                               if ('@DisabledOnJre' == concatenarPalavras):
                                   concatenarPalavras              = ""
                                   achouAbreChaveDisabledOnJre     = False
                                   achouDisabledOnJre              = True
                                   naoEhDisabledOnJre              = False
                                   contDisabledOnJre               += 1
                                   contarLetrasDisabledOnJre       = 0
                                   barraPraComentarioDisabledOnJre = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @DisabledOnJre
                   if (barraPraComentarioDisabledOnJre != True):
                       if ((len("@DisabledOnJre") == contarLetrasDisabledOnJre) or (len("@DisabledOnJre") == contarLetrasDisabledOnJre - 1)):
                           if ('@DisabledOnJre' == concatenarPalavras):
                               concatenarPalavras          = ""
                               contarLetrasDisabledOnJre   = 0
                               achouAbreChaveDisabledOnJre = False
                               achouDisabledOnJre          = True
                               contDisabledOnJre           += 1
             
       achouArrobaDisabledOnJre        = False
       achouAspasDisabledOnJre         = False
       barraPraComentarioDisabledOnJre = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@EnabledIfSystemProperty' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioEnabledIfSystemProperty = True
               elif (letra == '"'):
                     achouAspasEnabledIfSystemProperty = True
               elif (letra == "@"):
                     flagEnabledIfSystemProperty        = True
                     achouArrobaEnabledIfSystemProperty = True
                     break
           
           if (barraPraComentarioEnabledIfSystemProperty != True):
               if (achouAspasEnabledIfSystemProperty != True):
                   contarLetrasEnabledIfSystemProperty = 0
                   contarAspas                         = 0
                   naoEhEnabledIfSystemProperty        = None
                   concatenarPalavras                  = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagEnabledIfSystemProperty == True) and (achouArrobaEnabledIfSystemProperty == True)):
                               if (letra == "@"):
                                   if ((naoEhEnabledIfSystemProperty == True) and (contarLetrasEnabledIfSystemProperty == 24)):
                                       if ('@EnabledIfSystemProperty' == concatenarPalavras):
                                           achouAbreChaveEnabledIfSystemProperty = False
                                           achouEnabledIfSystemProperty          = True
                                           naoEhEnabledIfSystemProperty          = False
                                           contEnabledIfSystemProperty           += 1
                                           contarLetrasEnabledIfSystemProperty   = 1
                                           concatenarPalavras                    = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasEnabledIfSystemProperty = 1
                                       achouArrobaEnabledIfSystemProperty  = True
                                       concatenarPalavras                  = ""
                                       
                                   contarLetrasEnabledIfSystemProperty = 1
                                   concatenarPalavras                  += letra
                                   
                               elif (achouArrobaEnabledIfSystemProperty == True):
                                     if (contarLetrasEnabledIfSystemProperty == 24):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@EnabledIfSystemProperty' == concatenarPalavras):
                                                 achouAbreChaveEnabledIfSystemProperty = False
                                                 achouEnabledIfSystemProperty          = True
                                                 naoEhEnabledIfSystemProperty          = False
                                                 contEnabledIfSystemProperty           += 1
                                                 contarLetrasEnabledIfSystemProperty   = 0
                                                 concatenarPalavras                    = ""
                                             if (letra == "("):
                                                 concatenarPalavras                 = ""
                                                 flagEnabledIfSystemProperty        = False
                                                 achouArrobaEnabledIfSystemProperty = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasEnabledIfSystemProperty += 1
                                             naoEhEnabledIfSystemProperty        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras                 = ""
                                             flagEnabledIfSystemProperty        = False
                                             achouArrobaEnabledIfSystemProperty = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasEnabledIfSystemProperty = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasEnabledIfSystemProperty += 1
                                             naoEhEnabledIfSystemProperty        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasEnabledIfSystemProperty = True
                                   contarAspas                       += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas                       -= 2
                                   achouAspasEnabledIfSystemProperty = False
                                   
                               if (achouAspasEnabledIfSystemProperty != True):
                                   if (letra == ")"):
                                       flagEnabledIfSystemProperty        = True 
                                       achouArrobaEnabledIfSystemProperty = True
                                   elif (letra == "@"):
                                         concatenarPalavras                  = ""
                                         concatenarPalavras                  += letra
                                         contarLetrasEnabledIfSystemProperty = 1
                                         flagEnabledIfSystemProperty         = True
                                         achouArrobaEnabledIfSystemProperty  = True
                                     
                       else:
                           if ((naoEhEnabledIfSystemProperty == True) and (contarLetrasEnabledIfSystemProperty == 24)):
                               if ('@EnabledIfSystemProperty' == concatenarPalavras):
                                   concatenarPalavras                        = ""
                                   achouAbreChaveEnabledIfSystemProperty     = False
                                   achouEnabledIfSystemProperty              = True
                                   naoEhEnabledIfSystemProperty              = False
                                   contEnabledIfSystemProperty               += 1
                                   contarLetrasEnabledIfSystemProperty       = 0
                                   barraPraComentarioEnabledIfSystemProperty = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @EnabledIfSystemProperty
                   if (barraPraComentarioEnabledIfSystemProperty != True):
                       if ((len("@EnabledIfSystemProperty") == contarLetrasEnabledIfSystemProperty) or (len("@EnabledIfSystemProperty") == contarLetrasEnabledIfSystemProperty - 1)):
                           if ('@EnabledIfSystemProperty' == concatenarPalavras):
                               concatenarPalavras                    = "" 
                               contarLetrasEnabledIfSystemProperty   = 0                               
                               achouAbreChaveEnabledIfSystemProperty = False
                               achouEnabledIfSystemProperty          = True
                               contEnabledIfSystemProperty           += 1
             
       achouArrobaEnabledIfSystemProperty        = False
       achouAspasEnabledIfSystemProperty         = False
       barraPraComentarioEnabledIfSystemProperty = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@DisabledIfSystemProperty' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioDisabledIfSystemProperty = True
               elif (letra == '"'):
                     achouAspasDisabledIfSystemProperty = True
               elif (letra == "@"):
                     flagDisabledIfSystemProperty        = True
                     achouArrobaDisabledIfSystemProperty = True
                     break
           
           if (barraPraComentarioDisabledIfSystemProperty != True):
               if (achouAspasDisabledIfSystemProperty != True):
                   contarLetrasDisabledIfSystemProperty = 0
                   contarAspas                          = 0
                   naoEhDisabledIfSystemProperty        = None
                   concatenarPalavras                   = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagDisabledIfSystemProperty == True) and (achouArrobaDisabledIfSystemProperty == True)):
                               if (letra == "@"):
                                   if ((naoEhDisabledIfSystemProperty == True) and (contarLetrasDisabledIfSystemProperty == 25)):
                                       if ('@DisabledIfSystemProperty' == concatenarPalavras):
                                           achouAbreChaveDisabledIfSystemProperty = False
                                           achouDisabledIfSystemProperty          = True
                                           naoEhDisabledIfSystemProperty          = False
                                           contDisabledIfSystemProperty           += 1
                                           contarDisabledIfSystemProperty         = 1
                                           concatenarPalavras                     = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasDisabledIfSystemProperty = 1
                                       achouArrobaDisabledIfSystemProperty  = True
                                       concatenarPalavras                   = ""
                                   
                                   contarLetrasDisabledIfSystemProperty = 1
                                   concatenarPalavras                   += letra
                                   
                               elif (achouArrobaDisabledIfSystemProperty == True):
                                     if (contarLetrasDisabledIfSystemProperty == 25):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@DisabledIfSystemProperty' == concatenarPalavras):
                                                 achouAbreChaveDisabledIfSystemProperty = False
                                                 achouDisabledIfSystemProperty          = True
                                                 naoEhDisabledIfSystemProperty          = False
                                                 contDisabledIfSystemProperty           += 1
                                                 contarLetrasDisabledIfSystemProperty   = 0
                                                 concatenarPalavras                     = ""
                                             if (letra == "("):
                                                 concatenarPalavras                  = ""
                                                 flagDisabledIfSystemProperty        = False
                                                 achouArrobaDisabledIfSystemProperty = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasDisabledIfSystemProperty += 1
                                             naoEhDisabledIfSystemProperty        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras                  = ""
                                             flagDisabledIfSystemProperty        = False
                                             achouArrobaDisabledIfSystemProperty = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasDisabledIfSystemProperty = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasDisabledIfSystemProperty += 1
                                             naoEhDisabledIfSystemProperty        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasDisabledIfSystemProperty = True
                                   contarAspas                        += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas                        -= 2
                                   achouAspasDisabledIfSystemProperty = False
                                   
                               if (achouAspasDisabledIfSystemProperty != True):
                                   if (letra == ")"):
                                       flagDisabledIfSystemProperty        = True 
                                       achouArrobaDisabledIfSystemProperty = True
                                   elif (letra == "@"):
                                         concatenarPalavras                   = ""
                                         concatenarPalavras                   += letra
                                         contarLetrasDisabledIfSystemProperty = 1
                                         flagDisabledIfSystemProperty         = True
                                         achouArrobaDisabledIfSystemProperty  = True
                                     
                       else:
                           if ((naoEhDisabledIfSystemProperty == True) and (contarLetrasDisabledIfSystemProperty == 25)):
                               if ('@DisabledIfSystemProperty' == concatenarPalavras):
                                   concatenarPalavras                         = ""
                                   achouAbreChaveDisabledIfSystemProperty     = False
                                   achouDisabledIfSystemProperty              = True
                                   naoEhDisabledIfSystemProperty              = False
                                   contDisabledIfSystemProperty               += 1
                                   contarLetrasDisabledIfSystemProperty       = 0
                                   barraPraComentarioDisabledIfSystemProperty = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @DisabledIfSystemProperty
                   if (barraPraComentarioDisabledIfSystemProperty != True):
                       if ((len("@DisabledIfSystemProperty") == contarLetrasDisabledIfSystemProperty) or (len("@DisabledIfSystemProperty") == contarLetrasDisabledIfSystemProperty - 1)):
                           if ('@DisabledIfSystemProperty' == concatenarPalavras):
                               concatenarPalavras                     = ""
                               contarLetrasDisabledIfSystemProperty   = 0
                               achouAbreChaveDisabledIfSystemProperty = False
                               achouDisabledIfSystemProperty          = True
                               contDisabledIfSystemProperty           += 1
             
       achouArrobaDisabledIfSystemProperty        = False
       achouAspasDisabledIfSystemProperty         = False
       barraPraComentarioDisabledIfSystemProperty = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@EnabledIfEnvironmentVariable' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioEnabledIfEnvironmentVariable = True
               elif (letra == '"'):
                     achouAspasEnabledIfEnvironmentVariable = True
               elif (letra == "@"):
                     flagEnabledIfEnvironmentVariable        = True
                     achouArrobaEnabledIfEnvironmentVariable = True
                     break
           
           if (barraPraComentarioEnabledIfEnvironmentVariable != True):
               if (achouAspasEnabledIfEnvironmentVariable != True):
                   contarLetrasEnabledIfEnvironmentVariable = 0
                   contarAspas                              = 0
                   naoEhEnabledIfEnvironmentVariable        = None
                   concatenarPalavras                       = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagEnabledIfEnvironmentVariable == True) and (achouArrobaEnabledIfEnvironmentVariable == True)):
                               if (letra == "@"):
                                   if ((naoEhEnabledIfEnvironmentVariable == True) and (contarLetrasEnabledIfEnvironmentVariable == 29)):
                                       if ('@EnabledIfEnvironmentVariable' == concatenarPalavras):
                                           achouAbreChaveEnabledIfEnvironmentVariable = False
                                           achouEnabledIfEnvironmentVariable          = True
                                           naoEhEnabledIfEnvironmentVariable          = False
                                           contEnabledIfEnvironmentVariable           += 1
                                           contarLetrasEnabledIfEnvironmentVariable   = 1
                                           concatenarPalavras                         = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasEnabledIfEnvironmentVariable = 1
                                       achouArrobaEnabledIfEnvironmentVariable  = True
                                       concatenarPalavras                       = ""
                                       
                                   contarLetrasEnabledIfEnvironmentVariable = 1
                                   concatenarPalavras                       += letra
                                   
                               elif (achouArrobaEnabledIfEnvironmentVariable == True):
                                     if (contarLetrasEnabledIfEnvironmentVariable == 29):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@EnabledIfEnvironmentVariable' == concatenarPalavras):
                                                 achouAbreChaveEnabledIfEnvironmentVariable = False
                                                 achouEnabledIfEnvironmentVariable          = True
                                                 naoEhEnabledIfEnvironmentVariable          = False
                                                 contEnabledIfEnvironmentVariable           += 1
                                                 contarLetrasEnabledIfEnvironmentVariable   = 0
                                                 concatenarPalavras                         = ""
                                             if (letra == "("):
                                                 concatenarPalavras                      = ""
                                                 flagEnabledIfEnvironmentVariable        = False
                                                 achouArrobaEnabledIfEnvironmentVariable = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasEnabledIfEnvironmentVariable += 1
                                             naoEhEnabledIfEnvironmentVariable        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras                      = ""
                                             flagEnabledIfEnvironmentVariable        = False
                                             achouArrobaEnabledIfEnvironmentVariable = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasEnabledIfEnvironmentVariable = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasEnabledIfEnvironmentVariable += 1
                                             naoEhEnabledIfEnvironmentVariable        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasEnabledIfEnvironmentVariable = True
                                   contarAspas                            += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas                            -= 2
                                   achouAspasEnabledIfEnvironmentVariable = False
                                   
                               if (achouAspasEnabledIfEnvironmentVariable != True):
                                   if (letra == ")"):
                                       flagEnabledIfEnvironmentVariable        = True 
                                       achouArrobaEnabledIfEnvironmentVariable = True
                                   elif (letra == "@"):
                                         concatenarPalavras                       = ""
                                         concatenarPalavras                       += letra
                                         contarLetrasEnabledIfEnvironmentVariable = 1
                                         flagEnabledIfEnvironmentVariable         = True
                                         achouArrobaEnabledIfEnvironmentVariable  = True
                                     
                       else:
                           if ((naoEhEnabledIfEnvironmentVariable == True) and (contarLetrasEnabledIfEnvironmentVariable == 29)):
                               if ('@EnabledIfEnvironmentVariable' == concatenarPalavras):
                                   concatenarPalavras                             = ""
                                   achouAbreChaveEnabledIfEnvironmentVariable     = False
                                   achouEnabledIfEnvironmentVariable              = True
                                   naoEhEnabledIfEnvironmentVariable              = False
                                   contEnabledIfEnvironmentVariable               += 1
                                   contarLetrasEnabledIfEnvironmentVariable       = 0
                                   barraPraComentarioEnabledIfEnvironmentVariable = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @EnabledIfEnvironmentVariable
                   if (barraPraComentarioEnabledIfEnvironmentVariable != True):
                       if ((len("@EnabledIfEnvironmentVariable") == contarLetrasEnabledIfEnvironmentVariable) or (len("@EnabledIfEnvironmentVariable") == contarLetrasEnabledIfEnvironmentVariable - 1)):
                           if ('@EnabledIfEnvironmentVariable' == concatenarPalavras):
                               concatenarPalavras                         = ""
                               contarLetrasEnabledIfEnvironmentVariable   = 0
                               achouAbreChaveEnabledIfEnvironmentVariable = False
                               achouEnabledIfEnvironmentVariable          = True
                               contEnabledIfEnvironmentVariable           += 1
             
       achouArrobaEnabledIfEnvironmentVariable        = False
       achouAspasEnabledIfEnvironmentVariable         = False
       barraPraComentarioEnabledIfEnvironmentVariable = False 
              
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@DisabledIfEnvironmentVariable' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioDisabledIfEnvironmentVariable = True
               elif (letra == '"'):
                     achouAspasDisabledIfEnvironmentVariable = True
               elif (letra == "@"):
                     flagDisabledIfEnvironmentVariable        = True
                     achouArrobaDisabledIfEnvironmentVariable = True
                     break
           
           if (barraPraComentarioDisabledIfEnvironmentVariable != True):
               if (achouAspasDisabledIfEnvironmentVariable != True):
                   contarLetrasDisabledIfEnvironmentVariable = 0
                   contarAspas                               = 0
                   naoEhDisabledIfEnvironmentVariable        = None
                   concatenarPalavras                        = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagDisabledIfEnvironmentVariable == True) and (achouArrobaDisabledIfEnvironmentVariable == True)):
                               if (letra == "@"):
                                   if ((naoEhDisabledIfEnvironmentVariable == True) and (contarLetrasDisabledIfEnvironmentVariable == 30)):
                                       if ('@DisabledIfEnvironmentVariable' == concatenarPalavras):
                                           achouAbreChaveDisabledIfEnvironmentVariable = False
                                           achouDisabledIfEnvironmentVariable          = True
                                           naoEhDisabledIfEnvironmentVariable          = False
                                           contDisabledIfEnvironmentVariable           += 1
                                           contarLetrasDisabledIfEnvironmentVariable   = 1
                                           concatenarPalavras                          = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasDisabledIfEnvironmentVariable = 1
                                       achouArrobaDisabledIfEnvironmentVariable  = True
                                       concatenarPalavras                        = ""
                                   
                                   contarLetrasDisabledIfEnvironmentVariable = 1
                                   concatenarPalavras                        += letra
                                   
                               elif (achouArrobaDisabledIfEnvironmentVariable == True):
                                     if (contarLetrasDisabledIfEnvironmentVariable == 30):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@DisabledIfEnvironmentVariable' == concatenarPalavras):
                                                 achouAbreChaveDisabledIfEnvironmentVariable = False
                                                 achouDisabledIfEnvironmentVariable          = True
                                                 naoEhDisabledIfEnvironmentVariable          = False
                                                 contDisabledIfEnvironmentVariable           += 1
                                                 contarLetrasDisabledIfEnvironmentVariable   = 0
                                                 concatenarPalavras                          = ""
                                             if (letra == "("):
                                                 concatenarPalavras                       = ""
                                                 flagDisabledIfEnvironmentVariable        = False
                                                 achouArrobaDisabledIfEnvironmentVariable = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasDisabledIfEnvironmentVariable += 1
                                             naoEhDisabledIfEnvironmentVariable        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras                       = ""
                                             flagDisabledIfEnvironmentVariable        = False
                                             achouArrobaDisabledIfEnvironmentVariable = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasDisabledIfEnvironmentVariable = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasDisabledIfEnvironmentVariable += 1
                                             naoEhDisabledIfEnvironmentVariable        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasDisabledIfEnvironmentVariable = True
                                   contarAspas                             += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas                             -= 2
                                   achouAspasDisabledIfEnvironmentVariable = False
                                   
                               if (achouAspasDisabledIfEnvironmentVariable != True):
                                   if (letra == ")"):
                                       flagDisabledIfEnvironmentVariable        = True 
                                       achouArrobaDisabledIfEnvironmentVariable = True
                                   elif (letra == "@"):
                                         concatenarPalavras                        = ""
                                         concatenarPalavras                        += letra
                                         contarLetrasDisabledIfEnvironmentVariable = 1
                                         flagDisabledIfEnvironmentVariable         = True
                                         achouArrobaDisabledIfEnvironmentVariable  = True
                                     
                       else:
                           if ((naoEhDisabledIfEnvironmentVariable == True) and (contarLetrasDisabledIfEnvironmentVariable == 30)):
                               if ('@DisabledIfEnvironmentVariable' == concatenarPalavras):
                                   concatenarPalavras                              = ""
                                   achouAbreChaveDisabledIfEnvironmentVariable     = False
                                   achouDisabledIfEnvironmentVariable              = True
                                   naoEhDisabledIfEnvironmentVariable              = False
                                   contDisabledIfEnvironmentVariable               += 1
                                   contarLetrasDisabledIfEnvironmentVariable       = 0
                                   barraPraComentarioDisabledIfEnvironmentVariable = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @DisabledIfEnvironmentVariable
                   if (barraPraComentarioDisabledIfEnvironmentVariable != True):
                       if ((len("@DisabledIfEnvironmentVariable") == contarLetrasDisabledIfEnvironmentVariable) or (len("@DisabledIfEnvironmentVariable") == contarLetrasDisabledIfEnvironmentVariable - 1)):
                           if ('@DisabledIfEnvironmentVariable' == concatenarPalavras):
                               concatenarPalavras                          = ""
                               contarLetrasDisabledIfEnvironmentVariable   = 0
                               achouAbreChaveDisabledIfEnvironmentVariable = False
                               achouDisabledIfEnvironmentVariable          = True
                               contDisabledIfEnvironmentVariable           += 1
             
       achouArrobaDisabledIfEnvironmentVariable        = False
       achouAspasDisabledIfEnvironmentVariable         = False
       barraPraComentarioDisabledIfEnvironmentVariable = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@EnabledIf' in line:
           tamanho = (len(line) - 1)
           #Verifica se a linha da assinatura e um comentario
           for letra in line:
               if (letra == "/"):
                   barraPraComentarioEnabledIf = True
               elif (letra == '"'):
                     achouAspasEnabledIf = True
               elif (letra == "@"):
                     break
                     
           if '@EnabledIfEnvironmentVariable' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioEnabledIfEnvironmentVariable = True
                   elif (letra == "@"):
                         break
                         
           if '@EnabledIfSystemProperty' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioEnabledIfSystemProperty = True
                   elif (letra == "@"):
                         break
                                       
           if ((barraPraComentarioEnabledIf != barraPraComentarioEnabledIfEnvironmentVariable) and
              (barraPraComentarioEnabledIf  != barraPraComentarioEnabledIfSystemProperty)):
               for letra in line:
                   if (letra == "/"):
                       contarComentarioEnabledIf += 1
                   elif (letra == " ") or (letra == "	"):
                         contarComentarioEnabledIf += 1
                   else:
                       if (contarLetrasEnabledIf <= 10):
                           contarLetrasEnabledIf += 1
                       else:
                           contarComentarioEnabledIf += 1

           if (len("@EnabledIf") != (tamanho - (contarComentarioEnabledIf - 1)) and (barraPraComentarioEnabledIf == False)):
               for letra in line:
                   if ((letra == " ")or(letra == "	")):
                       contarAssinaturaEnabledIf += 1
                   elif (letra == "/"):
                         contarAssinaturaEnabledIf += 1
        
               for letra in line:
                   if (letra == "/"):
                       achouBarraEnabledIf = True
                   elif (achouBarraEnabledIf == True):
                         if ((letra != " ")and(letra != "	")):
                             contarAssinaturaEnabledIf += 1
                             decrementaEnabledIf       = True 
                             
               if (decrementaEnabledIf == True):
                   if (len("@EnabledIf") == (tamanho - (contarAssinaturaEnabledIf - 1))):
                       achouAbreChaveEnabledIf = False
                       achouEnabledIf          = True
                       contEnabledIf           += 1
               else:
                   if (len("@EnabledIf") == (tamanho - contarAssinaturaEnabledIf)):
                       achouAbreChaveEnabledIf = False
                       achouEnabledIf          = True
                       contEnabledIf           += 1

               if (achouEnabledIf != True):
                   contarLetrasEnabledIf = 0
                   contarAspas           = 0
                   naoEhEnabledIf        = None
                   concatenarPalavras    = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagEnabledIf == True) and (achouArrobaEnabledIf == True)):
                               if (letra == "@"):
                                   if ((naoEhEnabledIf == True) and (contarLetrasEnabledIf == 10)):
                                       if ('@EnabledIf' == concatenarPalavras):
                                           achouAbreChaveEnabledIf = False
                                           achouEnabledIf          = True
                                           naoEhEnabledIf          = False
                                           contEnabledIf           += 1
                                           contarLetrasEnabledIf   = 1
                                           concatenarPalavras      = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasEnabledIf = 1
                                       achouArrobaEnabledIf  = True
                                       concatenarPalavras    = ""
                                   
                                   contarLetrasEnabledIf = 1
                                   concatenarPalavras    += letra
                                   
                               elif (achouArrobaEnabledIf == True):
                                     if (contarLetrasEnabledIf == 10):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@EnabledIf' == concatenarPalavras):
                                                 achouAbreChaveEnabledIf = False
                                                 achouEnabledIf          = True
                                                 naoEhEnabledIf          = False
                                                 contEnabledIf           += 1
                                                 contarLetrasEnabledIf   = 0
                                                 concatenarPalavras      = ""
                                             if (letra == "("):
                                                 concatenarPalavras   = ""
                                                 flagEnabledIf        = False
                                                 achouArrobaEnabledIf = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasEnabledIf += 1
                                             naoEhEnabledIf        = False
                                             
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras   = ""
                                             flagEnabledIf        = False
                                             achouArrobaEnabledIf = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasEnabledIf = 0
                                             
                                             if ((letra != " ")and(letra != "   ")):                                             
                                                 concatenarPalavras += letra
                                             
                                             contarLetrasEnabledIf += 1
                                             naoEhEnabledIf        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasEnabledIf = True
                                   contarAspas         += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas         -= 2
                                   achouAspasEnabledIf = False
                                   
                               if (achouAspasEnabledIf != True):
                                   if (letra == ")"):
                                       flagEnabledIf        = True 
                                       achouArrobaEnabledIf = True
                                   elif (letra == "@"):
                                         concatenarPalavras    = ""
                                         concatenarPalavras    += letra
                                         contarLetrasEnabledIf = 1
                                         flagEnabledIf         = True
                                         achouArrobaEnabledIf  = True
                                     
                       else:
                           if ((naoEhEnabledIf == True) and (contarLetrasEnabledIf == 10)):
                               if ('@EnabledIf' == concatenarPalavras):
                                   concatenarPalavras          = ""
                                   achouAbreChaveEnabledIf     = False
                                   achouEnabledIf              = True
                                   naoEhEnabledIf              = False
                                   contEnabledIf               += 1
                                   contarLetrasEnabledIf       = 0
                                   barraPraComentarioEnabledIf = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @EnabledIf
                   if (barraPraComentarioEnabledIf != True):
                       if ((len("@EnabledIf") == contarLetrasEnabledIf) or (len("@EnabledIf") == contarLetrasEnabledIf - 1)):
                           if ('@EnabledIf' == concatenarPalavras):
                               concatenarPalavras      = ""
                               contarLetrasEnabledIf   = 0
                               achouAbreChaveEnabledIf = False
                               achouEnabledIf          = True
                               contEnabledIf           += 1
       
       #Inicializando os valores
       contarAssinaturaEnabledIf = 0
       achouBarraEnabledIf       = False
       achouArrobaEnabledIf      = False
       achouAspasEnabledIf       = False
       decrementaEnabledIf       = False
       
       achouEnabledIf = False
       
       contarComentarioEnabledIf = 0
       contarLetrasEnabledIf     = 1        
       barraPraComentarioEnabledIf                    = False
       barraPraComentarioEnabledIfEnvironmentVariable = False
       barraPraComentarioEnabledIfSystemProperty      = False

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@DisabledIf' in line:
           tamanho = (len(line) - 1)
           #Verifica se a linha da assinatura e um comentario
           for letra in line:
               if (letra == "/"):
                   barraPraComentarioDisabledIf = True
               elif (letra == '"'):
                     achouAspasDisabledIf = True
               elif (letra == "@"):
                     break
                     
           if '@DisabledIfSystemProperty' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioDisabledIfSystemProperty = True
                   elif (letra == "@"):
                         break
                         
           if '@DisabledIfEnvironmentVariable' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioDisabledIfEnvironmentVariable = True
                   elif (letra == "@"):
                         break
                                       
           if ((barraPraComentarioDisabledIf != barraPraComentarioDisabledIfSystemProperty) and
              (barraPraComentarioDisabledIf  != barraPraComentarioDisabledIfEnvironmentVariable)):
               for letra in line:
                   if (letra == "/"):
                       contarComentarioDisabledIf += 1
                   elif (letra == " ") or (letra == "	"):
                         contarComentarioDisabledIf += 1
                   else:
                       if (contarLetrasDisabledIf <= 11):
                           contarLetrasDisabledIf += 1
                       else:
                           contarComentarioDisabledIf += 1

           if (len("@DisabledIf") != (tamanho - (contarComentarioDisabledIf - 1)) and (barraPraComentarioDisabledIf == False)):
               for letra in line:
                   if ((letra == " ")or(letra == "	")):
                       contarAssinaturaDisabledIf += 1
                   elif (letra == "/"):
                         contarAssinaturaDisabledIf += 1
        
               for letra in line:
                   if (letra == "/"):
                       achouBarraDisabledIf = True
                   elif (achouBarraDisabledIf == True):
                         if ((letra != " ")and(letra != "	")):
                             contarAssinaturaDisabledIf += 1
                             decrementaDisabledIf       = True 
                             
               if (decrementaDisabledIf == True):
                   if (len("@DisabledIf") == (tamanho - (contarAssinaturaDisabledIf - 1))):
                       achouAbreChaveDisabledIf = False
                       achouDisabledIf          = True
                       contDisabledIf           += 1
               else:
                   if (len("@DisabledIf") == (tamanho - contarAssinaturaDisabledIf)):
                       achouAbreChaveDisabledIf = False
                       achouDisabledIf          = True
                       contDisabledIf           += 1

               if (achouDisabledIf != True):
                   contarLetrasDisabledIf = 0
                   contarAspas            = 0
                   naoEhDisabledIf        = None
                   concatenarPalavras     = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagDisabledIf == True) and (achouArrobaDisabledIf == True)):
                               if (letra == "@"):
                                   if ((naoEhDisabledIf == True) and (contarLetrasDisabledIf == 11)):
                                       if ('@DisabledIf' == concatenarPalavras):
                                           achouAbreChaveDisabledIf = False
                                           achouDisabledIf          = True
                                           naoEhDisabledIf          = False
                                           contDisabledIf           += 1
                                           contarLetrasDisabledIf   = 1
                                           concatenarPalavras       = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasDisabledIf = 1
                                       achouArrobaDisabledIf  = True
                                       concatenarPalavras     = ""
                                   
                                   contarLetrasDisabledIf = 1
                                   concatenarPalavras     += letra
                                   
                               elif (achouArrobaDisabledIf == True):
                                     if (contarLetrasDisabledIf == 11):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@DisabledIf' == concatenarPalavras):
                                                 achouAbreChaveDisabledIf = False
                                                 achouDisabledIf          = True
                                                 naoEhDisabledIf          = False
                                                 contDisabledIf           += 1
                                                 contarLetrasDisabledIf   = 0
                                                 concatenarPalavras       = ""
                                             if (letra == "("):
                                                 concatenarPalavras    = ""
                                                 flagDisabledIf        = False
                                                 achouArrobaDisabledIf = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasDisabledIf += 1
                                             naoEhDisabledIf        = False
                                             
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras    = ""
                                             flagDisabledIf        = False
                                             achouArrobaDisabledIf = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasDisabledIf = 0
                                             
                                             if ((letra != " ")and(letra != "   ")):                                             
                                                 concatenarPalavras += letra
                                             
                                             contarLetrasDisabledIf += 1
                                             naoEhDisabledIf        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasDisabledIf = True
                                   contarAspas          += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas          -= 2
                                   achouAspasDisabledIf = False
                                   
                               if (achouAspasDisabledIf != True):
                                   if (letra == ")"):
                                       flagDisabledIf        = True 
                                       achouArrobaDisabledIf = True
                                   elif (letra == "@"):
                                         concatenarPalavras     = ""
                                         concatenarPalavras     += letra
                                         contarLetrasDisabledIf = 1
                                         flagDisabledIf         = True
                                         achouArrobaDisabledIf  = True
                                     
                       else:
                           if ((naoEhDisabledIf == True) and (contarLetrasDisabledIf == 11)):
                               if ('@DisabledIf' == concatenarPalavras):
                                   concatenarPalavras           = ""
                                   achouAbreChaveDisabledIf     = False
                                   achouDisabledIf              = True
                                   naoEhDisabledIf              = False
                                   contDisabledIf               += 1
                                   contarLetrasDisabledIf       = 0
                                   barraPraComentarioDisabledIf = True
                           else:
                               if (contarAspas == 0):
                                   break
                                   
                   #Verifica a comparacao da igualdade da assinatura @DisabledIf
                   if (barraPraComentarioDisabledIf != True):
                       if ((len("@DisabledIf") == contarLetrasDisabledIf) or (len("@DisabledIf") == contarLetrasDisabledIf - 1)):
                           if ('@DisabledIf' == concatenarPalavras):
                               concatenarPalavras       = ""
                               contarLetrasDisabledIf   = 0
                               achouAbreChaveDisabledIf = False
                               achouDisabledIf          = True
                               contDisabledIf           += 1
       
       #Inicializando os valores
       contarAssinaturaDisabledIf = 0
       achouBarraDisabledIf       = False
       achouArrobaDisabledIf      = False
       achouAspasDisabledIf       = False
       decrementaDisabledIf       = False
       
       achouDisabledIf = False
       
       contarComentarioDisabledIf = 0
       contarLetrasDisabledIf     = 1        
       barraPraComentarioDisabledIf                    = False
       barraPraComentarioDisabledIfSystemProperty      = False
       barraPraComentarioDisabledIfEnvironmentVariable = False

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@Fast' in line:
           tamanho = (len(line) - 1)
           #Verifica se a linha da assinatura e um comentario
           for letra in line:
               if (letra == "/"):
                   barraPraComentarioFast = True
               elif (letra == '"'):
                     achouAspasFast = True
               elif (letra == "@"):
                     break
                     
           if '@FastTest' in line:
               for letra in line:
                   if (letra == "/"):
                       barraPraComentarioFastTest = True
                   elif (letra == "@"):
                         break
                                                  
           #Só entra na condição se a assinatura for um comentário
           if (barraPraComentarioFast != barraPraComentarioFastTest):
               for letra in line:
                   if (letra == "/"):
                       contarComentarioFast += 1
                   elif (letra == " ") or (letra == "	"):
                         contarComentarioFast += 1
                   else:
                       if (contarLetrasFast <= 5):
                           contarLetrasFast += 1
                       else:
                           contarComentarioFast += 1
           #Só entra na condição  com a comparação e validação das mesmas assinaturas @Fast
           if (len("@Fast") != (tamanho - (contarComentarioFast - 1)) and (barraPraComentarioFast == False)):     
               #A assinatura não sendo comentario sai verificando o que vem depois do mesmo               
               for letra in line:
                   if ((letra == " ")or(letra == "	")):
                       contarAssinaturaFast += 1
                   elif (letra == "/"):
                         contarAssinaturaFast += 1
        
               for letra in line:
                   if (letra == "/"):
                       achouBarraFast = True
                   elif (achouBarraFast == True):
                         if ((letra != " ")and(letra != "	")):
                             contarAssinaturaFast += 1
                             decrementaFast       = True
                             
               if (decrementaFast == True):
                   if (len("@Fast") == (tamanho - (contarAssinaturaFast - 1))):                 
                       achouAbreChaveFast = False
                       achouFast          = True  
                       contFast           += 1
               else:
                   if (len("@Fast") == (tamanho - contarAssinaturaFast)):
                       achouAbreChaveFast = False
                       achouFast          = True  
                       contFast           += 1

               if (achouFast != True):
                   contarLetrasFast   = 0
                   contarAspas        = 0
                   naoEhFast          = None
                   concatenarPalavras = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagFast == True) and (achouArrobaFast == True)):
                               if (letra == "@"):
                                   if ((naoEhFast == True) and (contarLetrasFast == 5)):
                                       if ('@Fast' == concatenarPalavras):
                                           achouAbreChaveFast = False
                                           achouFast          = True
                                           naoEhFast          = False
                                           contFast           += 1
                                           contarLetrasFast   = 1
                                           concatenarPalavras = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasFast   = 1
                                       achouArrobaFast    = True
                                       concatenarPalavras = ""
                                   
                                   contarLetrasFast   = 1
                                   concatenarPalavras += letra
                                   
                               elif (achouArrobaFast == True):
                                     if (contarLetrasFast == 5):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@Fast' == concatenarPalavras):
                                                 achouAbreChaveFast = False
                                                 achouFast          = True
                                                 naoEhFast          = False
                                                 contFast           += 1
                                                 contarLetrasFast   = 0
                                                 concatenarPalavras = ""
                                             if (letra == "("):
                                                 concatenarPalavras = ""
                                                 flagFast           = False
                                                 achouArrobaFast    = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasFast += 1
                                             naoEhFast        = False
                                             
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras = ""
                                             flagFast           = False
                                             achouArrobaFast    = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasFast = 0
                                             
                                             if ((letra != " ")and(letra != "   ")):                                             
                                                 concatenarPalavras += letra
                                             
                                             contarLetrasFast += 1
                                             naoEhFast        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasFast = True
                                   contarAspas    += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas    -= 2
                                   achouAspasFast = False
                                   
                               if (achouAspasFast != True):
                                   if (letra == ")"):
                                       flagFast        = True 
                                       achouArrobaFast = True
                                   elif (letra == "@"):
                                         concatenarPalavras = ""
                                         concatenarPalavras += letra
                                         contarLetrasFast   = 1
                                         flagFast           = True
                                         achouArrobaFast    = True
                                     
                       else:
                           if ((naoEhFast == True) and (contarLetrasFast == 5)):
                               if ('@Fast' == concatenarPalavras):
                                   concatenarPalavras     = ""
                                   achouAbreChaveFast     = False
                                   achouFast              = True
                                   naoEhFast              = False
                                   contFast               += 1
                                   contarLetrasFast       = 0
                                   barraPraComentarioFast = True
                           else:
                               if (contarAspas == 0):
                                   break
                   
                   #Verifica a comparacao da igualdade da assinatura @Fast
                   if (barraPraComentarioFast != True):
                       if ((len("@Fast") == contarLetrasFast) or (len("@Fast") == contarLetrasFast - 1)):
                           if ('@Fast' == concatenarPalavras):
                               concatenarPalavras = ""
                               contarLetrasFast   = 0
                               achouAbreChaveFast = False
                               achouFast          = True
                               contFast           += 1
       
       #Inicializando os valores
       contarAssinaturaFast = 0
       achouBarraFast       = False
       achouArrobaFast      = False
       achouAspasFast       = False
       decrementaFast       = False
       
       achouFast = False
       
       contarComentarioFast = 0
       contarLetrasFast     = 1        
       barraPraComentarioFast     = False
       barraPraComentarioFastTest = False      
   
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@FastTest' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioFastTest = True
               elif (letra == '"'):
                     achouAspasFastTest = True
               elif (letra == "@"):
                     flagFastTest        = True
                     achouArrobaFastTest = True
                     break
           
           if (barraPraComentarioFastTest != True):
               if (achouAspasFastTest != True):
                   contarLetrasFastTest = 0
                   contarAspas          = 0
                   naoEhFastTest        = None
                   concatenarPalavras   = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagFastTest == True) and (achouArrobaFastTest == True)):
                               if (letra == "@"):
                                   if ((naoEhFastTest == True) and (contarLetrasFastTest == 9)):
                                       if ('@FastTest' == concatenarPalavras):
                                           achouAbreChaveFastTest = False
                                           achouFastTest          = True
                                           naoEhFastTest          = False
                                           contFastTest           += 1
                                           contarLetrasFastTest   = 1
                                           concatenarPalavras     = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasFastTest = 1
                                       achouArrobaFastTest  = True
                                       concatenarPalavras   = ""
                                       
                                   contarLetrasFastTest = 1
                                   concatenarPalavras   += letra
                                   
                               elif (achouArrobaFastTest == True):
                                     if (contarLetrasFastTest == 9):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@FastTest' == concatenarPalavras):
                                                 achouAbreChaveFastTest = False
                                                 achouFastTest          = True
                                                 naoEhFastTest          = False
                                                 contFastTest           += 1
                                                 contarLetrasFastTest   = 0
                                                 concatenarPalavras     = ""
                                             if (letra == "("):
                                                 concatenarPalavras  = ""
                                                 flagFastTest        = False
                                                 achouArrobaFastTest = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasFastTest += 1
                                             naoEhFastTest        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras  = ""
                                             flagFastTest        = False
                                             achouArrobaFastTest = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasFastTest = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasFastTest += 1
                                             naoEhFastTest        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasFastTest = True
                                   contarAspas        += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas        -= 2
                                   achouAspasFastTest = False
                                   
                               if (achouAspasFastTest != True):
                                   if (letra == ")"):
                                       flagFastTest        = True 
                                       achouArrobaFastTest = True
                                   elif (letra == "@"):
                                         concatenarPalavras   = ""
                                         concatenarPalavras   += letra
                                         contarLetrasFastTest = 1
                                         flagFastTest         = True
                                         achouArrobaFastTest  = True
                                     
                       else:
                           if ((naoEhFastTest == True) and (contarLetrasFastTest == 9)):
                               if ('@FastTest' == concatenarPalavras):
                                   concatenarPalavras         = ""
                                   achouAbreChaveFastTest     = False
                                   achouFastTest              = True
                                   naoEhFastTest              = False
                                   contFastTest               += 1
                                   contarLetrasFastTest       = 0
                                   barraPraComentarioFastTest = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @FastTest
                   if (barraPraComentarioFastTest != True):
                       if ((len("@FastTest") == contarLetrasFastTest) or (len("@FastTest") == contarLetrasFastTest - 1)):
                           if ('@FastTest' == concatenarPalavras):
                               concatenarPalavras     = ""
                               contarLetrasFastTest   = 0
                               achouAbreChaveFastTest = False
                               achouFastTest          = True
                               contFastTest           += 1
             
       achouArrobaFastTest        = False
       achouAspasFastTest         = False
       barraPraComentarioFastTest = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@NullSource' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioNullSource = True
               elif (letra == '"'):
                     achouAspasNullSource = True
               elif (letra == "@"):
                     flagNullSource        = True
                     achouArrobaNullSource = True
                     break
           
           if (barraPraComentarioNullSource != True):
               if (achouAspasNullSource != True):
                   contarLetrasNullSource = 0
                   contarAspas            = 0
                   naoEhNullSource        = None
                   concatenarPalavras     = ""
                   
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagNullSource == True) and (achouArrobaNullSource == True)):
                               if (letra == "@"):
                                   if ((naoEhNullSource == True) and (contarLetrasNullSource == 11)):
                                       if ('@NullSource' == concatenarPalavras):
                                           achouAbreChaveNullSource = False
                                           achouNullSource          = True
                                           naoEhNullSource          = False
                                           contNullSource           += 1
                                           contarLetrasNullSource   = 1
                                           concatenarPalavras       = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasNullSource = 1
                                       achouArrobaNullSource  = True
                                       concatenarPalavras     = ""
                                   
                                   contarLetrasNullSource = 1
                                   concatenarPalavras     += letra
                                   
                               elif (achouArrobaNullSource == True):
                                     if (contarLetrasNullSource == 11):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@NullSource' == concatenarPalavras):
                                                 achouAbreChaveNullSource = False
                                                 achouNullSource          = True
                                                 naoEhNullSource          = False
                                                 contNullSource           += 1
                                                 contarLetrasNullSource   = 0
                                                 concatenarPalavras       = ""
                                             if (letra == "("):
                                                 concatenarPalavras    = ""
                                                 flagNullSource        = False
                                                 achouArrobaNullSource = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasNullSource += 1
                                             naoEhNullSource        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras    = ""
                                             flagNullSource        = False
                                             achouArrobaNullSource = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasNullSource = 0
                                             
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasNullSource += 1
                                             naoEhNullSource        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasNullSource = True
                                   contarAspas          += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas          -= 2
                                   achouAspasNullSource = False
                                   
                               if (achouAspasNullSource != True):
                                   if (letra == ")"):
                                       flagNullSource        = True 
                                       achouArrobaNullSource = True
                                   elif (letra == "@"):
                                         concatenarPalavras     = ""
                                         concatenarPalavras     += letra
                                         contarLetrasNullSource = 1
                                         flagNullSource         = True
                                         achouArrobaNullSource  = True
                                     
                       else:
                           if ((naoEhNullSource == True) and (contarLetrasNullSource == 11)):
                               if ('@NullSource' == concatenarPalavras):
                                   concatenarPalavras           = ""
                                   achouAbreChaveNullSource     = False
                                   achouNullSource              = True
                                   naoEhNullSource              = False
                                   contNullSource               += 1
                                   contarLetrasNullSource       = 0
                                   barraPraComentarioNullSource = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @NullSource
                   if (barraPraComentarioNullSource != True):
                       if ((len("@NullSource") == contarLetrasNullSource) or (len("@NullSource") == contarLetrasNullSource - 1)):
                           if ('@NullSource' == concatenarPalavras):
                               concatenarPalavras       = ""
                               contarLetrasNullSource   = 0
                               achouAbreChaveNullSource = False
                               achouNullSource          = True
                               contNullSource           += 1
             
       achouArrobaNullSource        = False
       achouAspasNullSource         = False
       barraPraComentarioNullSource = False 
              
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@EmptySource' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioEmptySource = True
               elif (letra == '"'):
                     achouAspasEmptySource = True
               elif (letra == "@"):
                     flagEmptySource        = True
                     achouArrobaEmptySource = True
                     break
           
           if (barraPraComentarioEmptySource != True):
               if (achouAspasEmptySource != True):
                   contarLetrasEmptySource = 0
                   contarAspas             = 0
                   naoEhEmptySource        = None
                   concatenarPalavras      = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagEmptySource == True) and (achouArrobaEmptySource == True)):
                               if (letra == "@"):
                                   if ((naoEhEmptySource == True) and (contarLetrasEmptySource == 12)):
                                       if ('@EmptySource' == concatenarPalavras):
                                           achouAbreChaveEmptySource = False
                                           achouEmptySource          = True
                                           naoEhEmptySource          = False
                                           contEmptySource           += 1
                                           contarLetrasEmptySource   = 1
                                           concatenarPalavras        = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasEmptySource = 1
                                       achouArrobaEmptySource  = True
                                       concatenarPalavras      = ""
                                       
                                   contarLetrasEmptySource = 1
                                   concatenarPalavras      += letra
                                   
                               elif (achouArrobaEmptySource == True):
                                     if (contarLetrasEmptySource == 12):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@EmptySource' == concatenarPalavras):
                                                 achouAbreChaveEmptySource = False
                                                 achouEmptySource          = True
                                                 naoEhEmptySource          = False
                                                 contEmptySource           += 1
                                                 contarLetrasEmptySource   = 0
                                                 concatenarPalavras        = ""
                                             if (letra == "("):
                                                 concatenarPalavras     = ""
                                                 flagEmptySource        = False
                                                 achouArrobaEmptySource = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasEmptySource += 1
                                             naoEhEmptySource        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras     = ""
                                             flagEmptySource        = False
                                             achouArrobaEmptySource = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasEmptySource = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasEmptySource += 1
                                             naoEhEmptySource        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasEmptySource = True
                                   contarAspas           += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas           -= 2
                                   achouAspasEmptySource = False
                                   
                               if (achouAspasEmptySource != True):
                                   if (letra == ")"):
                                       flagEmptySource        = True 
                                       achouArrobaEmptySource = True
                                   elif (letra == "@"):
                                         concatenarPalavras      = ""
                                         concatenarPalavras      += letra
                                         contarLetrasEmptySource = 1
                                         flagEmptySource         = True
                                         achouArrobaEmptySource  = True
                                     
                       else:
                           if ((naoEhEmptySource == True) and (contarLetrasEmptySource == 12)):
                               if ('@EmptySource' == concatenarPalavras):
                                   concatenarPalavras            = ""
                                   achouAbreChaveEmptySource     = False
                                   achouEmptySource              = True
                                   naoEhEmptySource              = False
                                   contEmptySource               += 1
                                   contarLetrasEmptySource       = 0
                                   barraPraComentarioEmptySource = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @EmptySource
                   if (barraPraComentarioEmptySource != True):
                       if ((len("@EmptySource") == contarLetrasEmptySource) or (len("@EmptySource") == contarLetrasEmptySource - 1)):
                           if ('@EmptySource' == concatenarPalavras):
                               concatenarPalavras        = ""
                               contarLetrasEmptySource   = 0
                               achouAbreChaveEmptySource = False
                               achouEmptySource          = True
                               contEmptySource           += 1
             
       achouArrobaEmptySource        = False
       achouAspasEmptySource         = False
       barraPraComentarioEmptySource = False

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@NullAndEmptySource' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioNullAndEmptySource = True
               elif (letra == '"'):
                     achouAspasNullAndEmptySource = True
               elif (letra == "@"):
                     flagNullAndEmptySource        = True
                     achouArrobaNullAndEmptySource = True
                     break
           
           if (barraPraComentarioNullAndEmptySource != True):
               if (achouAspasNullAndEmptySource != True):
                   contarLetrasNullAndEmptySource = 0
                   contarAspas                    = 0
                   naoEhNullAndEmptySource        = None
                   concatenarPalavras             = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagNullAndEmptySource == True) and (achouArrobaNullAndEmptySource == True)):
                               if (letra == "@"):
                                   if ((naoEhNullAndEmptySource == True) and (contarLetrasNullAndEmptySource == 19)):
                                       if ('@NullAndEmptySource' == concatenarPalavras):
                                           achouAbreChaveNullAndEmptySource = False
                                           achouNullAndEmptySource          = True
                                           naoEhNullAndEmptySource          = False
                                           contNullAndEmptySource           += 1
                                           contarLetrasNullAndEmptySource   = 1
                                           concatenarPalavras               = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasNullAndEmptySource = 1
                                       achouArrobaNullAndEmptySource  = True
                                       concatenarPalavras             = ""
                                       
                                   contarLetrasNullAndEmptySource = 1
                                   concatenarPalavras             += letra
                                   
                               elif (achouArrobaNullAndEmptySource == True):
                                     if (contarLetrasNullAndEmptySource == 19):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@NullAndEmptySource' == concatenarPalavras):
                                                 achouAbreChaveNullAndEmptySource = False
                                                 achouNullAndEmptySource          = True
                                                 naoEhNullAndEmptySource          = False
                                                 contNullAndEmptySource           += 1
                                                 contarLetrasNullAndEmptySource   = 0
                                                 concatenarPalavras               = ""
                                             if (letra == "("):
                                                 concatenarPalavras            = ""
                                                 flagNullAndEmptySource        = False
                                                 achouArrobaNullAndEmptySource = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasNullAndEmptySource += 1
                                             naoEhNullAndEmptySource        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras            = ""
                                             flagNullAndEmptySource        = False
                                             achouArrobaNullAndEmptySource = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasNullAndEmptySource = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasNullAndEmptySource += 1
                                             naoEhNullAndEmptySource        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasNullAndEmptySource = True
                                   contarAspas                  += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas                  -= 2
                                   achouAspasNullAndEmptySource = False
                                   
                               if (achouAspasNullAndEmptySource != True):
                                   if (letra == ")"):
                                       flagNullAndEmptySource        = True 
                                       achouArrobaNullAndEmptySource = True
                                   elif (letra == "@"):
                                         concatenarPalavras             = ""
                                         concatenarPalavras             += letra
                                         contarLetrasNullAndEmptySource = 1
                                         flagNullAndEmptySource         = True
                                         achouArrobaNullAndEmptySource  = True
                                         
                                     
                       else:
                           if ((naoEhNullAndEmptySource == True) and (contarLetrasNullAndEmptySource == 19)):
                               if ('@NullAndEmptySource' == concatenarPalavras):
                                   concatenarPalavras                   = ""
                                   achouAbreChaveNullAndEmptySource     = False
                                   achouNullAndEmptySource              = True
                                   naoEhNullAndEmptySource              = False
                                   contNullAndEmptySource               += 1
                                   contarLetrasNullAndEmptySource       = 0
                                   barraPraComentarioNullAndEmptySource = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @NullAndEmptySource
                   if (barraPraComentarioNullAndEmptySource != True):
                       if ((len("@NullAndEmptySource") == contarLetrasNullAndEmptySource) or (len("@NullAndEmptySource") == contarLetrasNullAndEmptySource - 1)):
                           if ('@NullAndEmptySource' == concatenarPalavras):
                               concatenarPalavras               = ""
                               contarLetrasNullAndEmptySource   = 0
                               achouAbreChaveNullAndEmptySource = False
                               achouNullAndEmptySource          = True
                               contNullAndEmptySource           += 1
             
       achouArrobaNullAndEmptySource        = False
       achouAspasNullAndEmptySource         = False
       barraPraComentarioNullAndEmptySource = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@EnumSource' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioEnumSource = True
               elif (letra == '"'):
                     achouAspasEnumSource = True
               elif (letra == "@"):
                     flagEnumSource        = True
                     achouArrobaEnumSource = True
                     break
           
           if (barraPraComentarioEnumSource != True):
               if (achouAspasEnumSource != True):
                   contarLetrasEnumSource = 0
                   contarAspas            = 0
                   naoEhEnumSource        = None
                   concatenarPalavras     = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagEnumSource == True) and (achouArrobaEnumSource == True)):
                               if (letra == "@"):
                                   if ((naoEhEnumSource == True) and (contarLetrasEnumSource == 11)):
                                       if ('@EnumSource' == concatenarPalavras):
                                           achouAbreChaveEnumSource = False
                                           achouEnumSource          = True
                                           naoEhEnumSource          = False
                                           contEnumSource           += 1
                                           contarLetrasEnumSource   = 1
                                           concatenarPalavras       = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasEnumSource = 1
                                       achouArrobaEnumSource  = True
                                       concatenarPalavras     = ""
                                       
                                   contarLetrasEnumSource = 1
                                   concatenarPalavras     += letra
                                   
                               elif (achouArrobaEnumSource == True):
                                     if (contarLetrasEnumSource == 11):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@EnumSource' == concatenarPalavras):
                                                 achouAbreChaveEnumSource = False
                                                 achouEnumSource          = True
                                                 naoEhEnumSource          = False
                                                 contEnumSource           += 1
                                                 contarLetrasEnumSource   = 0
                                                 concatenarPalavras       = ""
                                             if (letra == "("):
                                                 concatenarPalavras    = ""
                                                 flagEnumSource        = False
                                                 achouArrobaEnumSource = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasEnumSource += 1
                                             naoEhEnumSource        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras    = ""
                                             flagEnumSource        = False
                                             achouArrobaEnumSource = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasEnumSource = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasEnumSource += 1
                                             naoEhEnumSource        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasEnumSource = True
                                   contarAspas          += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas          -= 2
                                   achouAspasEnumSource = False
                                   
                               if (achouAspasEnumSource != True):
                                   if (letra == ")"):
                                       flagEnumSource        = True 
                                       achouArrobaEnumSource = True
                                   elif (letra == "@"):
                                         concatenarPalavras     = ""
                                         concatenarPalavras     += letra
                                         contarLetrasEnumSource = 1
                                         flagEnumSource         = True
                                         achouArrobaEnumSource  = True
                                     
                       else:
                           if ((naoEhEnumSource == True) and (contarLetrasEnumSource == 11)):
                               if ('@EnumSource' == concatenarPalavras):
                                   concatenarPalavras           = ""
                                   achouAbreChaveEnumSource     = False
                                   achouEnumSource              = True
                                   naoEhEnumSource              = False
                                   contEnumSource               += 1
                                   contarLetrasEnumSource       = 0
                                   barraPraComentarioEnumSource = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @EnumSource
                   if (barraPraComentarioEnumSource != True):
                       if ((len("@EnumSource") == contarLetrasEnumSource) or (len("@EnumSource") == contarLetrasEnumSource - 1)):
                           if ('@EnumSource' == concatenarPalavras):
                               concatenarPalavras       = ""
                               contarLetrasEnumSource   = 0
                               achouAbreChaveEnumSource = False
                               achouEnumSource          = True
                               contEnumSource           += 1
             
       achouArrobaEnumSource        = False
       achouAspasEnumSource         = False
       barraPraComentarioEnumSource = False  

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@MethodSource' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioMethodSource = True
               elif (letra == '"'):
                     achouAspasMethodSource = True
               elif (letra == "@"):
                     flagMethodSource        = True
                     achouArrobaMethodSource = True
                     break
           
           if (barraPraComentarioMethodSource != True):
               if (achouAspasMethodSource != True):
                   contarLetrasMethodSource = 0
                   contarAspas              = 0
                   naoEhMethodSource        = None
                   concatenarPalavras       = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagMethodSource == True) and (achouArrobaMethodSource == True)):
                               if (letra == "@"):
                                   if ((naoEhMethodSource == True) and (contarLetrasMethodSource == 13)):
                                       if ('@MethodSource' == concatenarPalavras):
                                           achouAbreChaveMethodSource = False
                                           achouMethodSource          = True
                                           naoEhMethodSource          = False
                                           contMethodSource           += 1
                                           contarLetrasMethodSource   = 1
                                           concatenarPalavras         = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasMethodSource = 1
                                       achouArrobaMethodSource  = True
                                       concatenarPalavras       = ""
                                       
                                   contarLetrasMethodSource = 1
                                   concatenarPalavras       += letra
                                   
                               elif (achouArrobaMethodSource == True):
                                     if (contarLetrasMethodSource == 13):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@MethodSource' == concatenarPalavras):
                                                 achouAbreChaveMethodSource = False
                                                 achouMethodSource          = True
                                                 naoEhMethodSource          = False
                                                 contMethodSource           += 1
                                                 contarLetrasMethodSource   = 0
                                                 concatenarPalavras         = ""
                                             if (letra == "("):
                                                 concatenarPalavras      = ""
                                                 flagMethodSource        = False
                                                 achouArrobaMethodSource = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasMethodSource += 1
                                             naoEhMethodSource        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras      = ""
                                             flagMethodSource        = False
                                             achouArrobaMethodSource = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasMethodSource = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasMethodSource += 1
                                             naoEhMethodSource        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasMethodSource = True
                                   contarAspas            += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas            -= 2
                                   achouAspasMethodSource = False
                                   
                               if (achouAspasMethodSource != True):
                                   if (letra == ")"):
                                       flagMethodSource        = True 
                                       achouArrobaMethodSource = True
                                   elif (letra == "@"):
                                         concatenarPalavras       = ""
                                         concatenarPalavras       += letra
                                         contarLetrasMethodSource = 1
                                         flagMethodSource         = True
                                         achouArrobaMethodSource  = True
                                     
                       else:
                           if ((naoEhMethodSource == True) and (contarLetrasMethodSource == 13)):
                               if ('@MethodSource' == concatenarPalavras):
                                   concatenarPalavras             = ""
                                   achouAbreChaveMethodSource     = False
                                   achouMethodSource              = True
                                   naoEhMethodSource              = False
                                   contMethodSource               += 1
                                   contarLetrasMethodSource       = 0
                                   barraPraComentarioMethodSource = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @MethodSource
                   if (barraPraComentarioMethodSource != True):
                       if ((len("@MethodSource") == contarLetrasMethodSource) or (len("@MethodSource") == contarLetrasMethodSource - 1)):
                           if ('@MethodSource' == concatenarPalavras):
                               concatenarPalavras         = ""
                               contarLetrasMethodSource   = 0
                               achouAbreChaveMethodSource = False
                               achouMethodSource          = True
                               contMethodSource           += 1
             
       achouArrobaMethodSource        = False
       achouAspasMethodSource         = False
       barraPraComentarioMethodSource = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@CsvSource' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioCsvSource = True
               elif (letra == '"'):
                     achouAspasCsvSource = True
               elif (letra == "@"):
                     flagCsvSource        = True
                     achouArrobaCsvSource = True
                     break
           
           if (barraPraComentarioCsvSource != True):
               if (achouAspasCsvSource != True):
                   contarLetrasCsvSource = 0
                   contarAspas           = 0
                   naoEhCsvSource        = None
                   concatenarPalavras    = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagCsvSource == True) and (achouArrobaCsvSource == True)):
                               if (letra == "@"):
                                   if ((naoEhCsvSource == True) and (contarLetrasCsvSource == 10)):
                                       if ('@CsvSource' == concatenarPalavras):
                                           achouAbreChaveCsvSource = False
                                           achouCsvSource          = True
                                           naoEhCsvSource          = False
                                           contCsvSource           += 1
                                           contarLetrasCsvSource   = 1
                                           concatenarPalavras      = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasCsvSource = 1
                                       achouArrobaCsvSource  = True
                                       concatenarPalavras    = ""
                                       
                                   contarLetrasCsvSource = 1
                                   concatenarPalavras    += letra
                                   
                               elif (achouArrobaCsvSource == True):
                                     if (contarLetrasCsvSource == 10):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@CsvSource' == concatenarPalavras):
                                                 achouAbreChaveCsvSource = False
                                                 achouCsvSource          = True
                                                 naoEhCsvSource          = False
                                                 contCsvSource           += 1
                                                 contarLetrasCsvSource   = 0
                                                 concatenarPalavras      = ""
                                             if (letra == "("):
                                                 concatenarPalavras   = ""
                                                 flagCsvSource        = False
                                                 achouArrobaCsvSource = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasCsvSource += 1
                                             naoEhCsvSource        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras   = ""
                                             flagCsvSource        = False
                                             achouArrobaCsvSource = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasCsvSource = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasCsvSource += 1
                                             naoEhCsvSource        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasCsvSource = True
                                   contarAspas         += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas         -= 2
                                   achouAspasCsvSource = False
                                   
                               if (achouAspasCsvSource != True):
                                   if (letra == ")"):
                                       flagCsvSource        = True 
                                       achouArrobaCsvSource = True
                                   elif (letra == "@"):
                                         concatenarPalavras    = ""
                                         concatenarPalavras    += letra
                                         contarLetrasCsvSource = 1
                                         flagCsvSource         = True
                                         achouArrobaCsvSource  = True
                                     
                       else:
                           if ((naoEhCsvSource == True) and (contarLetrasCsvSource == 10)):
                               if ('@CsvSource' == concatenarPalavras):
                                   concatenarPalavras          = ""                             
                                   achouAbreChaveCsvSource     = False
                                   achouCsvSource              = True
                                   naoEhCsvSource              = False
                                   contCsvSource               += 1
                                   contarLetrasCsvSource       = 0
                                   barraPraComentarioCsvSource = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @CsvSource
                   if (barraPraComentarioCsvSource != True):
                       if ((len("@CsvSource") == contarLetrasCsvSource) or (len("@CsvSource") == contarLetrasCsvSource - 1)):
                           if ('@CsvSource' == concatenarPalavras):
                               concatenarPalavras      = ""
                               contarLetrasCsvSource   = 0
                               achouAbreChaveCsvSource = False
                               achouCsvSource          = True
                               contCsvSource           += 1
             
       achouArrobaCsvSource        = False
       achouAspasCsvSource         = False
       barraPraComentarioCsvSource = False 
   
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@CsvFileSource' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioCsvFileSource = True
               elif (letra == '"'):
                     achouAspasCsvFileSource = True
               elif (letra == "@"):
                     flagCsvFileSource        = True
                     achouArrobaCsvFileSource = True
                     break
           
           if (barraPraComentarioCsvFileSource != True):
               if (achouAspasCsvFileSource != True):
                   contarLetrasCsvFileSource = 0
                   contarAspas               = 0
                   naoEhCsvFileSource        = None
                   concatenarPalavras        = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagCsvFileSource == True) and (achouArrobaCsvFileSource == True)):
                               if (letra == "@"):
                                   if ((naoEhCsvFileSource == True) and (contarLetrasCsvFileSource == 14)):
                                       if ('@CsvFileSource' == concatenarPalavras):
                                           achouAbreChaveCsvFileSource = False
                                           achouCsvFileSource          = True
                                           naoEhCsvFileSource          = False
                                           contCsvFileSource           += 1
                                           contarLetrasCsvFileSource   = 1
                                           concatenarPalavras          = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasCsvFileSource = 1
                                       achouArrobaCsvFileSource  = True
                                       concatenarPalavras        = ""
                                       
                                   contarLetrasCsvFileSource = 1
                                   concatenarPalavras        += letra
                                   
                               elif (achouArrobaCsvFileSource == True):
                                     if (contarLetrasCsvFileSource == 14):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@CsvFileSource' == concatenarPalavras):
                                                 achouAbreChaveCsvFileSource = False
                                                 achouCsvFileSource          = True
                                                 naoEhCsvFileSource          = False
                                                 contCsvFileSource           += 1
                                                 contarLetrasCsvFileSource   = 0
                                                 concatenarPalavras          = ""
                                             if (letra == "("):
                                                 concatenarPalavras       = ""
                                                 flagCsvFileSource        = False
                                                 achouArrobaCsvFileSource = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasCsvFileSource += 1
                                             naoEhCsvFileSource        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras       = ""
                                             flagCsvFileSource        = False
                                             achouArrobaCsvFileSource = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasCsvFileSource = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasCsvFileSource += 1
                                             naoEhCsvFileSource        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasCsvFileSource = True
                                   contarAspas             += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas             -= 2
                                   achouAspasCsvFileSource = False
                                   
                               if (achouAspasCsvFileSource != True):
                                   if (letra == ")"):
                                       flagCsvFileSource        = True 
                                       achouArrobaCsvFileSource = True
                                   elif (letra == "@"):
                                         concatenarPalavras        = ""
                                         concatenarPalavras        += letra
                                         contarLetrasCsvFileSource = 1
                                         flagCsvFileSource         = True
                                         achouArrobaCsvFileSource  = True
                                     
                       else:
                           if ((naoEhCsvFileSource == True) and (contarLetrasCsvFileSource == 14)):
                               if ('@CsvFileSource' == concatenarPalavras):
                                   concatenarPalavras              = ""
                                   achouAbreChaveCsvFileSource     = False
                                   achouCsvFileSource              = True
                                   naoEhCsvFileSource              = False
                                   contCsvFileSource               += 1
                                   contarLetrasCsvFileSource       = 0
                                   barraPraComentarioCsvFileSource = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @CsvFileSource
                   if (barraPraComentarioCsvFileSource != True):
                       if ((len("@CsvFileSource") == contarLetrasCsvFileSource) or (len("@CsvFileSource") == contarLetrasCsvFileSource - 1)):
                           if ('@CsvFileSource' == concatenarPalavras):
                               concatenarPalavras          = ""
                               contarLetrasCsvFileSource   = 0
                               achouAbreChaveCsvFileSource = False
                               achouCsvFileSource          = True
                               contCsvFileSource           += 1
             
       achouArrobaCsvFileSource        = False
       achouAspasCsvFileSource         = False
       barraPraComentarioCsvFileSource = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@ArgumentsSource' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioArgumentsSource = True
               elif (letra == '"'):
                     achouAspasArgumentsSource = True
               elif (letra == "@"):
                     flagArgumentsSource        = True
                     achouArrobaArgumentsSource = True
                     break
           
           if (barraPraComentarioArgumentsSource != True):
               if (achouAspasArgumentsSource != True):
                   contarLetrasArgumentsSource = 0
                   contarAspas                 = 0
                   naoEhArgumentsSource        = None
                   concatenarPalavras          = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagArgumentsSource == True) and (achouArrobaArgumentsSource == True)):
                               if (letra == "@"):
                                   if ((naoEhArgumentsSource == True) and (contarLetrasArgumentsSource == 16)):
                                       if ('@ArgumentsSource' == concatenarPalavras):
                                           achouAbreChaveArgumentsSource = False
                                           achouArgumentsSource          = True
                                           naoEhArgumentsSource          = False
                                           contArgumentsSource           += 1
                                           contarLetrasArgumentsSource   = 1
                                           concatenarPalavras            = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasArgumentsSource = 1
                                       achouArrobaArgumentsSource  = True
                                       concatenarPalavras          = ""
                                   
                                   contarLetrasArgumentsSource = 1
                                   concatenarPalavras          += letra
                                   
                               elif (achouArrobaArgumentsSource == True):
                                     if (contarLetrasArgumentsSource == 16):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@ArgumentsSource' == concatenarPalavras):
                                                 achouAbreChaveArgumentsSource = False
                                                 achouArgumentsSource          = True
                                                 naoEhArgumentsSource          = False
                                                 contArgumentsSource           += 1
                                                 contarLetrasArgumentsSource   = 0
                                                 concatenarPalavras            = ""
                                             if (letra == "("):
                                                 concatenarPalavras         = ""
                                                 flagArgumentsSource        = False
                                                 achouArrobaArgumentsSource = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasArgumentsSource += 1
                                             naoEhArgumentsSource        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras         = ""
                                             flagArgumentsSource        = False
                                             achouArrobaArgumentsSource = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasArgumentsSource = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasArgumentsSource += 1
                                             naoEhArgumentsSource        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasArgumentsSource = True
                                   contarAspas               += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas               -= 2
                                   achouAspasArgumentsSource = False
                                   
                               if (achouAspasArgumentsSource != True):
                                   if (letra == ")"):
                                       flagArgumentsSource        = True 
                                       achouArrobaArgumentsSource = True
                                   elif (letra == "@"):
                                         concatenarPalavras          = ""
                                         concatenarPalavras          += letra
                                         contarLetrasArgumentsSource = 1
                                         flagArgumentsSource         = True
                                         achouArrobaArgumentsSource  = True
                                     
                       else:
                           if ((naoEhArgumentsSource == True) and (contarLetrasArgumentsSource == 16)):
                               if ('@ArgumentsSource' == concatenarPalavras):
                                   concatenarPalavras                = ""
                                   achouAbreChaveArgumentsSource     = False
                                   achouArgumentsSource              = True
                                   naoEhArgumentsSource              = False
                                   contArgumentsSource               += 1
                                   contarLetrasArgumentsSource       = 0
                                   barraPraComentarioArgumentsSource = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @ArgumentsSource
                   if (barraPraComentarioArgumentsSource != True):
                       if ((len("@ArgumentsSource") == contarLetrasArgumentsSource) or (len("@ArgumentsSource") == contarLetrasArgumentsSource - 1)):
                           if ('@ArgumentsSource' == concatenarPalavras):
                               concatenarPalavras            = ""
                               contarLetrasArgumentsSource   = 0
                               achouAbreChaveArgumentsSource = False
                               achouArgumentsSource          = True
                               contArgumentsSource           += 1
             
       achouArrobaArgumentsSource        = False
       achouAspasArgumentsSource         = False
       barraPraComentarioArgumentsSource = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@AggregateWith' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioAggregateWith = True
               elif (letra == '"'):
                     achouAspasAggregateWith = True
               elif (letra == "@"):
                     flagAggregateWith        = True
                     achouArrobaAggregateWith = True
                     break
           
           if (barraPraComentarioAggregateWith != True):
               if (achouAspasAggregateWith != True):
                   contarLetrasAggregateWith = 0
                   contarAspas               = 0
                   naoEhAggregateWith        = None
                   concatenarPalavras        = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagAggregateWith == True) and (achouArrobaAggregateWith == True)):
                               if (letra == "@"):
                                   if ((naoEhAggregateWith == True) and (contarLetrasAggregateWith == 14)):
                                       if ('@AggregateWith' == concatenarPalavras):
                                           achouAbreChaveAggregateWith = False
                                           achouAggregateWith          = True
                                           naoEhAggregateWith          = False
                                           contAggregateWith           += 1
                                           contarLetrasAggregateWith   = 1
                                           concatenarPalavras          = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasAggregateWith = 1
                                       achouArrobaAggregateWith  = True
                                       concatenarPalavras        = ""
                                       
                                   contarLetrasAggregateWith = 1
                                   concatenarPalavras        += letra
                                   
                               elif (achouArrobaAggregateWith == True):
                                     if (contarLetrasAggregateWith == 14):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@AggregateWith' == concatenarPalavras):
                                                 achouAbreChaveAggregateWith = False
                                                 achouAggregateWith          = True
                                                 naoEhAggregateWith          = False
                                                 contAggregateWith           += 1
                                                 contarLetrasAggregateWith   = 0
                                                 concatenarPalavras          = ""
                                             if (letra == "("):
                                                 concatenarPalavras       = ""
                                                 flagAggregateWith        = False
                                                 achouArrobaAggregateWith = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasAggregateWith += 1
                                             naoEhAggregateWith        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras       = ""
                                             flagAggregateWith        = False
                                             achouArrobaAggregateWith = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasAggregateWith = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasAggregateWith += 1
                                             naoEhAggregateWith        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasAggregateWith = True
                                   contarAspas             += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas             -= 2
                                   achouAspasAggregateWith = False
                                   
                               if (achouAspasAggregateWith != True):
                                   if (letra == ")"):
                                       flagAggregateWith        = True 
                                       achouArrobaAggregateWith = True
                                   elif (letra == "@"):
                                         concatenarPalavras        = ""
                                         concatenarPalavras        += letra
                                         contarLetrasAggregateWith = 1
                                         flagAggregateWith         = True
                                         achouArrobaAggregateWith  = True
                                     
                       else:
                           if ((naoEhAggregateWith == True) and (contarLetrasAggregateWith == 14)):
                               if ('@AggregateWith' == concatenarPalavras):
                                   concatenarPalavras              = ""
                                   achouAbreChaveAggregateWith     = False
                                   achouAggregateWith              = True
                                   naoEhAggregateWith              = False
                                   contAggregateWith               += 1
                                   contarLetrasAggregateWith       = 0
                                   barraPraComentarioAggregateWith = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @AggregateWith
                   if (barraPraComentarioAggregateWith != True):
                       if ((len("@AggregateWith") == contarLetrasAggregateWith) or (len("@AggregateWith") == contarLetrasAggregateWith - 1)):
                           if ('@AggregateWith' == concatenarPalavras):
                               concatenarPalavras          = ""
                               contarLetrasAggregateWith   = 0
                               achouAbreChaveAggregateWith = False
                               achouAggregateWith          = True
                               contAggregateWith           += 1
             
       achouArrobaAggregateWith        = False
       achouAspasAggregateWith         = False
       barraPraComentarioAggregateWith = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@Execution' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioExecution = True
               elif (letra == '"'):
                     achouAspasExecution = True
               elif (letra == "@"):
                     flagExecution        = True
                     achouArrobaExecution = True
                     break
           
           if (barraPraComentarioExecution != True):
               if (achouAspasExecution != True):
                   contarLetrasExecution = 0
                   contarAspas           = 0
                   naoEhExecution        = None
                   concatenarPalavras    = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagExecution == True) and (achouArrobaExecution == True)):
                               if (letra == "@"):
                                   if ((naoEhExecution == True) and (contarLetrasExecution == 10)):
                                       if ('@Execution' == concatenarPalavras):
                                           achouAbreChaveExecution = False
                                           achouExecution          = True
                                           naoEhExecution          = False
                                           contExecution           += 1
                                           contarLetrasExecution   = 1
                                           concatenarPalavras      = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasExecution = 1
                                       achouArrobaExecution  = True
                                       concatenarPalavras    = ""
                                   
                                   contarLetrasExecution = 1
                                   concatenarPalavras    += letra
                                   
                               elif (achouArrobaExecution == True):
                                     if (contarLetrasExecution == 10):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@Execution' == concatenarPalavras):
                                                 achouAbreChaveExecution = False
                                                 achouExecution          = True
                                                 naoEhExecution          = False
                                                 contExecution           += 1
                                                 contarLetrasExecution   = 0
                                                 concatenarPalavras      = ""
                                             if (letra == "("):
                                                 concatenarPalavras   = ""
                                                 flagExecution        = False
                                                 achouArrobaExecution = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasExecution += 1
                                             naoEhExecution        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras   = ""
                                             flagExecution        = False
                                             achouArrobaExecution = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasExecution = 0
                                             
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasExecution += 1
                                             naoEhExecution        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasExecution = True
                                   contarAspas         += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas         -= 2
                                   achouAspasExecution = False
                                   
                               if (achouAspasExecution != True):
                                   if (letra == ")"):
                                       flagExecution        = True 
                                       achouArrobaExecution = True
                                   elif (letra == "@"):
                                         concatenarPalavras    = ""
                                         concatenarPalavras    += letra
                                         contarLetrasExecution = 1
                                         flagExecution         = True
                                         achouArrobaExecution  = True
                                     
                       else:
                           if ((naoEhExecution == True) and (contarLetrasExecution == 10)):
                               if ('@Execution' == concatenarPalavras):
                                   concatenarPalavras          = ""
                                   achouAbreChaveExecution     = False
                                   achouExecution              = True
                                   naoEhExecution              = False
                                   contExecution               += 1
                                   contarLetrasExecution       = 0
                                   barraPraComentarioExecution = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @Execution
                   if (barraPraComentarioExecution != True):
                       if ((len("@Execution") == contarLetrasExecution) or (len("@Execution") == contarLetrasExecution - 1)):
                           if ('@Execution' == concatenarPalavras):
                               concatenarPalavras      = ""
                               contarLetrasExecution   = 0
                               achouAbreChaveExecution = False
                               achouExecution          = True
                               contExecution           += 1
             
       achouArrobaExecution        = False
       achouAspasExecution         = False
       barraPraComentarioExecution = False 
   
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@ResourceLock' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioResourceLock = True
               elif (letra == '"'):
                     achouAspasResourceLock = True
               elif (letra == "@"):
                     flagResourceLock        = True
                     achouArrobaResourceLock = True
                     break
           
           if (barraPraComentarioResourceLock != True):
               if (achouAspasResourceLock != True):
                   contarLetrasResourceLock = 0
                   contarAspas              = 0
                   naoEhResourceLock        = None
                   concatenarPalavras       = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagResourceLock == True) and (achouArrobaResourceLock == True)):
                               if (letra == "@"):
                                   if ((naoEhResourceLock == True) and (contarLetrasResourceLock == 13)):
                                       if ('@ResourceLock' == concatenarPalavras):
                                           achouAbreChaveResourceLock = False
                                           achouResourceLock          = True
                                           naoEhResourceLock          = False
                                           contResourceLock           += 1
                                           contarLetrasResourceLock   = 1
                                           concatenarPalavras         = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasResourceLock = 1
                                       achouArrobaResourceLock  = True
                                       concatenarPalavras       = ""
                                       
                                   contarLetrasResourceLock = 1
                                   concatenarPalavras       += letra
                                   
                               elif (achouArrobaResourceLock == True):
                                     if (contarLetrasResourceLock == 13):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@ResourceLock' == concatenarPalavras):
                                                 achouAbreChaveResourceLock = False
                                                 achouResourceLock          = True
                                                 naoEhResourceLock          = False
                                                 contResourceLock           += 1
                                                 contarLetrasResourceLock   = 0
                                                 concatenarPalavras         = ""
                                             if (letra == "("):
                                                 concatenarPalavras      = ""
                                                 flagResourceLock        = False
                                                 achouArrobaResourceLock = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasResourceLock += 1
                                             naoEhResourceLock        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras      = ""
                                             flagResourceLock        = False
                                             achouArrobaResourceLock = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasResourceLock = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasResourceLock += 1
                                             naoEhResourceLock        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasResourceLock = True
                                   contarAspas            += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas            -= 2
                                   achouAspasResourceLock = False
                                   
                               if (achouAspasResourceLock != True):
                                   if (letra == ")"):
                                       flagResourceLock        = True 
                                       achouArrobaResourceLock = True
                                   elif (letra == "@"):
                                         concatenarPalavras       = ""
                                         concatenarPalavras       += letra
                                         contarLetrasResourceLock = 1
                                         flagResourceLock         = True
                                         achouArrobaResourceLock  = True
                                     
                       else:
                           if ((naoEhResourceLock == True) and (contarLetrasResourceLock == 13)):
                               if ('@ResourceLock' == concatenarPalavras):
                                   concatenarPalavras             = ""
                                   achouAbreChaveResourceLock     = False
                                   achouResourceLock              = True
                                   naoEhResourceLock              = False
                                   contResourceLock               += 1
                                   contarLetrasResourceLock       = 0
                                   barraPraComentarioResourceLock = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @ResourceLock
                   if (barraPraComentarioResourceLock != True):
                       if ((len("@ResourceLock") == contarLetrasResourceLock) or (len("@ResourceLock") == contarLetrasResourceLock - 1)):
                           if ('@ResourceLock' == concatenarPalavras):
                               concatenarPalavras         = ""
                               contarLetrasResourceLock   = 0
                               achouAbreChaveResourceLock = False
                               achouResourceLock          = True
                               contResourceLock           += 1
             
       achouArrobaResourceLock        = False
       achouAspasResourceLock         = False
       barraPraComentarioResourceLock = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@Ignore' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioIgnore = True
               elif (letra == '"'):
                     achouAspasIgnore = True
               elif (letra == "@"):
                     flagIgnore        = True
                     achouArrobaIgnore = True
                     break
           
           if (barraPraComentarioIgnore != True):
               if (achouAspasIgnore != True):
                   contarLetrasIgnore = 0
                   contarAspas        = 0
                   naoEhIgnore        = None
                   concatenarPalavras = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagIgnore == True) and (achouArrobaIgnore == True)):
                               if (letra == "@"):
                                   if ((naoEhIgnore == True) and (contarLetrasIgnore == 7)):
                                       if ('@Ignore' == concatenarPalavras):
                                           achouAbreChaveIgnore = False
                                           achouIgnore          = True
                                           naoEhIgnore          = False
                                           contIgnore           += 1
                                           contarLetrasIgnore   = 1
                                           concatenarPalavras   = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasIgnore = 1
                                       achouArrobaIgnore  = True
                                       concatenarPalavras = ""
                                       
                                   contarLetrasIgnore = 1
                                   concatenarPalavras += letra
                                   
                               elif (achouArrobaIgnore == True):
                                     if (contarLetrasIgnore == 7):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@Ignore' == concatenarPalavras):
                                                 achouAbreChaveIgnore = False
                                                 achouIgnore          = True
                                                 naoEhIgnore          = False
                                                 contIgnore           += 1
                                                 contarLetrasIgnore   = 0
                                                 concatenarPalavras   = ""
                                             if (letra == "("):
                                                 concatenarPalavras = ""
                                                 flagIgnore         = False
                                                 achouArrobaIgnore  = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasIgnore += 1
                                             naoEhIgnore        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras = ""
                                             flagIgnore         = False
                                             achouArrobaIgnore  = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasIgnore = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasIgnore += 1
                                             naoEhIgnore        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasIgnore = True
                                   contarAspas      += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas      -= 2
                                   achouAspasIgnore = False
                                   
                               if (achouAspasIgnore != True):
                                   if (letra == ")"):
                                       flagIgnore        = True 
                                       achouArrobaIgnore = True
                                   elif (letra == "@"):
                                         concatenarPalavras = ""
                                         concatenarPalavras += letra
                                         contarLetrasIgnore = 1
                                         flagIgnore         = True
                                         achouArrobaIgnore  = True
                                     
                       else:
                           if ((naoEhIgnore == True) and (contarLetrasIgnore == 7)):
                               if ('@Ignore' == concatenarPalavras):
                                   concatenarPalavras       = ""
                                   achouAbreChaveIgnore     = False
                                   achouIgnore              = True
                                   naoEhIgnore              = False
                                   contIgnore               += 1
                                   contarLetrasIgnore       = 0
                                   barraPraComentarioIgnore = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @Ignore
                   if (barraPraComentarioIgnore != True):
                       if ((len("@Ignore") == contarLetrasIgnore) or (len("@Ignore") == contarLetrasIgnore - 1)):
                           if ('@Ignore' == concatenarPalavras):
                               concatenarPalavras   = ""
                               contarLetrasIgnore   = 0
                               achouAbreChaveIgnore = False
                               achouIgnore          = True
                               contIgnore           += 1
             
       achouArrobaIgnore        = False
       achouAspasIgnore         = False
       barraPraComentarioIgnore = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@Category' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioCategory = True
               elif (letra == '"'):
                     achouAspasCategory = True
               elif (letra == "@"):
                     flagCategory        = True
                     achouArrobaCategory = True
                     break
           
           if (barraPraComentarioCategory != True):
               if (achouAspasCategory != True):
                   contarLetrasCategory = 0
                   contarAspas          = 0
                   naoEhCategory        = None
                   concatenarPalavras   = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagCategory == True) and (achouArrobaCategory == True)):
                               if (letra == "@"):
                                   if ((naoEhCategory == True) and (contarLetrasCategory == 9)):
                                       if ('@Category' == concatenarPalavras):
                                           achouAbreChaveCategory = False
                                           achouCategory          = True
                                           naoEhCategory          = False
                                           contCategory           += 1
                                           contarLetrasCategory   = 1
                                           concatenarPalavras     = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasCategory = 1
                                       achouArrobaCategory  = True
                                       concatenarPalavras   = ""
                                       
                                   contarLetrasCategory = 1
                                   concatenarPalavras   += letra
                                   
                               elif (achouArrobaCategory == True):
                                     if (contarLetrasCategory == 9):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@Category' == concatenarPalavras):
                                                 achouAbreChaveCategory = False
                                                 achouCategory          = True
                                                 naoEhCategory          = False
                                                 contCategory           += 1
                                                 contarLetrasCategory   = 0
                                                 concatenarPalavras     = ""
                                             if (letra == "("):
                                                 concatenarPalavras  = ""
                                                 flagCategory        = False
                                                 achouArrobaCategory = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasCategory += 1
                                             naoEhCategory        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras  = ""
                                             flagCategory        = False
                                             achouArrobaCategory = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasCategory = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasCategory += 1
                                             naoEhCategory        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasCategory = True
                                   contarAspas        += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas        -= 2
                                   achouAspasCategory = False
                                   
                               if (achouAspasCategory != True):
                                   if (letra == ")"):
                                       flagCategory        = True 
                                       achouArrobaCategory = True
                                   elif (letra == "@"):
                                         concatenarPalavras   = ""
                                         concatenarPalavras   += letra
                                         contarLetrasCategory = 1
                                         flagCategory         = True
                                         achouArrobaCategory  = True
                                     
                       else:
                           if ((naoEhCategory == True) and (contarLetrasCategory == 9)):
                               if ('@Category' == concatenarPalavras):
                                   concatenarPalavras         = ""
                                   achouAbreChaveCategory     = False
                                   achouCategory              = True
                                   naoEhCategory              = False
                                   contCategory               += 1
                                   contarLetrasCategory       = 0
                                   barraPraComentarioCategory = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @Category
                   if (barraPraComentarioCategory != True):
                       if ((len("@Category") == contarLetrasCategory) or (len("@Category") == contarLetrasCategory - 1)):
                           if ('@Category' == concatenarPalavras):
                               concatenarPalavras     = ""
                               contarLetrasCategory   = 0
                               achouAbreChaveCategory = False
                               achouCategory          = True
                               contCategory           += 1
             
       achouArrobaCategory        = False
       achouAspasCategory         = False
       barraPraComentarioCategory = False 
   
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@RunWith' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioRunWith = True
               elif (letra == '"'):
                     achouAspasRunWith = True
               elif (letra == "@"):
                     flagRunWith        = True
                     achouArrobaRunWith = True
                     break
           
           if (barraPraComentarioRunWith != True):
               if (achouAspasRunWith != True):
                   contarLetrasRunWith = 0
                   contarAspas         = 0
                   naoEhRunWith        = None
                   concatenarPalavras  = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagRunWith == True) and (achouArrobaRunWith == True)):
                               if (letra == "@"):
                                   if ((naoEhRunWith == True) and (contarLetrasRunWith == 8)):
                                       if ('@RunWith' == concatenarPalavras):
                                           achouAbreChaveRunWith = False
                                           achouRunWith          = True
                                           naoEhRunWith          = False
                                           contRunWith           += 1
                                           contarLetrasRunWith   = 1
                                           concatenarPalavras    = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasRunWith = 1
                                       achouArrobaRunWith  = True
                                       concatenarPalavras  = ""
                                       
                                   contarLetrasRunWith = 1
                                   concatenarPalavras  += letra
                                   
                               elif (achouArrobaRunWith == True):
                                     if (contarLetrasRunWith == 8):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@RunWith' == concatenarPalavras):
                                                 achouAbreChaveRunWith = False
                                                 achouRunWith          = True
                                                 naoEhRunWith          = False
                                                 contRunWith           += 1
                                                 contarLetrasRunWith   = 0
                                                 concatenarPalavras    = ""
                                             if (letra == "("):
                                                 concatenarPalavras = ""
                                                 flagRunWith        = False
                                                 achouArrobaRunWith = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasRunWith += 1
                                             naoEhRunWith        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras = ""
                                             flagRunWith        = False
                                             achouArrobaRunWith = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasRunWith = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasRunWith += 1
                                             naoEhRunWith        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasRunWith = True
                                   contarAspas       += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas       -= 2
                                   achouAspasRunWith = False
                                   
                               if (achouAspasRunWith != True):
                                   if (letra == ")"):
                                       flagRunWith        = True 
                                       achouArrobaRunWith = True
                                   elif (letra == "@"):
                                         concatenarPalavras  = ""
                                         concatenarPalavras  += letra
                                         contarLetrasRunWith = 1
                                         flagRunWith         = True
                                         achouArrobaRunWith  = True
                                     
                       else:
                           if ((naoEhRunWith == True) and (contarLetrasRunWith == 8)):
                               if ('@RunWith' == concatenarPalavras):
                                   concatenarPalavras        = ""
                                   achouAbreChaveRunWith     = False
                                   achouRunWith              = True
                                   naoEhRunWith              = False
                                   contRunWith               += 1
                                   contarLetrasRunWith       = 0
                                   barraPraComentarioRunWith = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @RunWith
                   if (barraPraComentarioRunWith != True):
                       if ((len("@RunWith") == contarLetrasRunWith) or (len("@RunWith") == contarLetrasRunWith - 1)):
                           if ('@RunWith' == concatenarPalavras):
                               concatenarPalavras    = ""
                               contarLetrasRunWith   = 0
                               achouAbreChaveRunWith = False
                               achouRunWith          = True
                               contRunWith           += 1
             
       achouArrobaRunWith        = False
       achouAspasRunWith         = False
       barraPraComentarioRunWith = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@Rule' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioRule = True
               elif (letra == '"'):
                     achouAspasRule = True
               elif (letra == "@"):
                     flagRule        = True
                     achouArrobaRule = True
                     break
           
           if (barraPraComentarioRule != True):
               if (achouAspasRule != True):
                   contarLetrasRule   = 0
                   contarAspas        = 0
                   naoEhRule          = None
                   concatenarPalavras = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagRule == True) and (achouArrobaRule == True)):
                               if (letra == "@"):
                                   if ((naoEhRule == True) and (contarLetrasRule == 5)):
                                       if ('@Rule' == concatenarPalavras):
                                           achouAbreChaveRule = False
                                           achouRule          = True
                                           naoEhRule          = False
                                           contRule           += 1
                                           contarLetrasRule   = 1
                                           concatenarPalavras = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasRule   = 1
                                       achouArrobaRule    = True
                                       concatenarPalavras = ""
                                       
                                   contarLetrasRule   = 1
                                   concatenarPalavras += letra
                                   
                               elif (achouArrobaRule == True):
                                     if (contarLetrasRule == 5):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@Rule' == concatenarPalavras):
                                                 achouAbreChaveRule = False
                                                 achouRule          = True
                                                 naoEhRule          = False
                                                 contRule           += 1
                                                 contarLetrasRule   = 0
                                                 concatenarPalavras = ""
                                             if (letra == "("):
                                                 concatenarPalavras = ""
                                                 flagRule           = False
                                                 achouArrobaRule    = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasRule += 1
                                             naoEhRule        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras = ""
                                             flagRule           = False
                                             achouArrobaRule    = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasRule = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasRule += 1
                                             naoEhRule        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasRule = True
                                   contarAspas    += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas    -= 2
                                   achouAspasRule = False
                                   
                               if (achouAspasRule != True):
                                   if (letra == ")"):
                                       flagRule        = True 
                                       achouArrobaRule = True
                                   elif (letra == "@"):
                                         concatenarPalavras = ""
                                         concatenarPalavras += letra
                                         contarLetrasRule   = 1
                                         flagRule           = True
                                         achouRule          = True
                                     
                       else:
                           if ((naoEhRule == True) and (contarLetrasRule == 5)):
                               if ('@Rule' == concatenarPalavras):
                                   concatenarPalavras     = ""
                                   achouAbreChaveRule     = False
                                   achouRule              = True
                                   naoEhRule              = False
                                   contRule               += 1
                                   contarLetrasRule       = 0
                                   barraPraComentarioRule = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @Rule
                   if (barraPraComentarioRule != True):
                       if ((len("@Rule") == contarLetrasRule) or (len("@Rule") == contarLetrasRule - 1)):
                           if ('@Rule' == concatenarPalavras):
                               concatenarPalavras = ""
                               contarLetrasRule   = 0
                               achouAbreChaveRule = False
                               achouRule          = True
                               contRule           += 1
             
       achouArrobaRule        = False
       achouAspasRule         = False
       barraPraComentarioRule = False 
       
   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@ClassRule' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioClassRule = True
               elif (letra == '"'):
                     achouAspasClassRule = True
               elif (letra == "@"):
                     flagClassRule        = True
                     achouArrobaClassRule = True
                     break
           
           if (barraPraComentarioClassRule != True):
               if (achouAspasClassRule != True):
                   contarLetrasClassRule = 0
                   contarAspas           = 0
                   naoEhClassRule        = None
                   concatenarPalavras    = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagClassRule == True) and (achouArrobaClassRule == True)):
                               if (letra == "@"):
                                   if ((naoEhClassRule == True) and (contarLetrasClassRule == 10)):
                                       if ('@ClassRule' == concatenarPalavras):
                                           achouAbreChaveClassRule = False
                                           achouClassRule          = True
                                           naoEhClassRule          = False
                                           contClassRule           += 1
                                           contarLetrasClassRule   = 1
                                           concatenarPalavras      = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasClassRule = 1
                                       achouArrobaClassRule  = True
                                       concatenarPalavras    = ""
                                       
                                   contarLetrasClassRule = 1
                                   concatenarPalavras    += letra
                                   
                               elif (achouArrobaClassRule == True):
                                     if (contarLetrasClassRule == 10):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@ClassRule' == concatenarPalavras):
                                                 achouAbreChaveClassRule = False
                                                 achouClassRule          = True
                                                 naoEhClassRule          = False
                                                 contClassRule           += 1
                                                 contarLetrasClassRule   = 0
                                                 concatenarPalavras      = ""
                                             if (letra == "("):
                                                 concatenarPalavras   = ""
                                                 flagClassRule        = False
                                                 achouArrobaClassRule = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasClassRule += 1
                                             naoEhClassRule        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras   = ""
                                             flagClassRule        = False
                                             achouArrobaClassRule = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasClassRule = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasClassRule += 1
                                             naoEhClassRule        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasClassRule = True
                                   contarAspas         += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas         -= 2
                                   achouAspasClassRule = False
                                   
                               if (achouAspasClassRule != True):
                                   if (letra == ")"):
                                       flagClassRule        = True 
                                       achouArrobaClassRule = True
                                   elif (letra == "@"):
                                         concatenarPalavras    = ""
                                         concatenarPalavras    += letra
                                         contarLetrasClassRule = 1
                                         flagClassRule         = True
                                         achouArrobaClassRule  = True
                                     
                       else:
                           if ((naoEhClassRule == True) and (contarLetrasClassRule == 10)):
                               if ('@ClassRule' == concatenarPalavras):
                                   concatenarPalavras          = ""
                                   achouAbreChaveClassRule     = False
                                   achouClassRule              = True
                                   naoEhClassRule              = False
                                   contClassRule               += 1
                                   contarLetrasClassRule       = 0
                                   barraPraComentarioClassRule = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @ClassRule
                   if (barraPraComentarioClassRule != True):
                       if ((len("@ClassRule") == contarLetrasClassRule) or (len("@ClassRule") == contarLetrasClassRule - 1)):
                           if ('@ClassRule' == concatenarPalavras):
                               concatenarPalavras      = ""
                               contarLetrasClassRule   = 0
                               achouAbreChaveClassRule = False
                               achouClassRule          = True
                               contClassRule           += 1
             
       achouArrobaClassRule        = False
       achouAspasClassRule         = False
       barraPraComentarioClassRule = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@EnableRuleMigrationSupport' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioEnableRuleMigrationSupport = True
               elif (letra == '"'):
                     achouAspasEnableRuleMigrationSupport = True
               elif (letra == "@"):
                     flagEnableRuleMigrationSupport        = True
                     achouArrobaEnableRuleMigrationSupport = True
                     break
           
           if (barraPraComentarioEnableRuleMigrationSupport != True):
               if (achouAspasEnableRuleMigrationSupport != True):
                   contarLetrasEnableRuleMigrationSupport = 0
                   contarAspas                            = 0
                   naoEhEnableRuleMigrationSupport        = None
                   concatenarPalavras                     = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagEnableRuleMigrationSupport == True) and (achouArrobaEnableRuleMigrationSupport == True)):
                               if (letra == "@"):
                                   if ((naoEhEnableRuleMigrationSupport == True) and (contarLetrasEnableRuleMigrationSupport == 27)):
                                       if ('@EnableRuleMigrationSupport' == concatenarPalavras):
                                           achouAbreChaveEnableRuleMigrationSupport = False
                                           achouEnableRuleMigrationSupport          = True
                                           naoEhEnableRuleMigrationSupport          = False
                                           contEnableRuleMigrationSupport           += 1
                                           contarLetrasEnableRuleMigrationSupport   = 1
                                           concatenarPalavras                       = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasEnableRuleMigrationSupport = 1
                                       achouArrobaEnableRuleMigrationSupport  = True
                                       concatenarPalavras                     = ""
                                       
                                   contarLetrasEnableRuleMigrationSupport = 1
                                   concatenarPalavras                     += letra
                                   
                               elif (achouArrobaEnableRuleMigrationSupport == True):
                                     if (contarLetrasEnableRuleMigrationSupport == 27):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@EnableRuleMigrationSupport' == concatenarPalavras):
                                                 achouAbreChaveEnableRuleMigrationSupport = False
                                                 achouEnableRuleMigrationSupport          = True
                                                 naoEhEnableRuleMigrationSupport          = False
                                                 contEnableRuleMigrationSupport           += 1
                                                 contarLetrasEnableRuleMigrationSupport   = 0
                                                 concatenarPalavras                       = ""
                                             if (letra == "("):
                                                 concatenarPalavras                    = ""
                                                 flagEnableRuleMigrationSupport        = False
                                                 achouArrobaEnableRuleMigrationSupport = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasEnableRuleMigrationSupport += 1
                                             naoEhEnableRuleMigrationSupport        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras                    = ""
                                             flagEnableRuleMigrationSupport        = False
                                             achouArrobaEnableRuleMigrationSupport = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasEnableRuleMigrationSupport = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasEnableRuleMigrationSupport += 1
                                             naoEhEnableRuleMigrationSupport        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasEnableRuleMigrationSupport = True
                                   contarAspas                          += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas                          -= 2
                                   achouAspasEnableRuleMigrationSupport = False
                                   
                               if (achouAspasEnableRuleMigrationSupport != True):
                                   if (letra == ")"):
                                       flagEnableRuleMigrationSupport        = True 
                                       achouArrobaEnableRuleMigrationSupport = True
                                   elif (letra == "@"):
                                         concatenarPalavras                     = ""
                                         concatenarPalavras                     += letra
                                         contarLetrasEnableRuleMigrationSupport = 1
                                         flagEnableRuleMigrationSupport         = True
                                         achouArrobaEnableRuleMigrationSupport  = True
                                     
                       else:
                           if ((naoEhEnableRuleMigrationSupport == True) and (contarLetrasEnableRuleMigrationSupport == 27)):
                               if ('@EnableRuleMigrationSupport' == concatenarPalavras):
                                   concatenarPalavras                           = ""
                                   achouAbreChaveEnableRuleMigrationSupport     = False
                                   achouEnableRuleMigrationSupport              = True
                                   naoEhEnableRuleMigrationSupport              = False
                                   contEnableRuleMigrationSupport               += 1
                                   contarLetrasEnableRuleMigrationSupport       = 0
                                   barraPraComentarioEnableRuleMigrationSupport = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @EnableRuleMigrationSupport
                   if (barraPraComentarioEnableRuleMigrationSupport != True):
                       if ((len("@EnableRuleMigrationSupport") == contarLetrasEnableRuleMigrationSupport) or (len("@EnableRuleMigrationSupport") == contarLetrasEnableRuleMigrationSupport - 1)):
                           if ('@EnableRuleMigrationSupport' == concatenarPalavras):
                               concatenarPalavras                       = ""
                               contarLetrasEnableRuleMigrationSupport   = 0
                               achouAbreChaveEnableRuleMigrationSupport = False
                               achouEnableRuleMigrationSupport          = True
                               contEnableRuleMigrationSupport           += 1
             
       achouArrobaEnableRuleMigrationSupport        = False
       achouAspasEnableRuleMigrationSupport         = False
       barraPraComentarioEnableRuleMigrationSupport = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@EnableJUnit4MigrationSupport' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioEnableJUnit4MigrationSupport = True
               elif (letra == '"'):
                     achouAspasEnableJUnit4MigrationSupport = True
               elif (letra == "@"):
                     flagEnableJUnit4MigrationSupport        = True
                     achouArrobaEnableJUnit4MigrationSupport = True
                     break
           
           if (barraPraComentarioEnableJUnit4MigrationSupport != True):
               if (achouAspasEnableJUnit4MigrationSupport != True):
                   contarLetrasEnableJUnit4MigrationSupport = 0
                   contarAspas                              = 0
                   naoEhEnableJUnit4MigrationSupport        = None
                   concatenarPalavras                       = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagEnableJUnit4MigrationSupport == True) and (achouArrobaEnableJUnit4MigrationSupport == True)):
                               if (letra == "@"):
                                   if ((naoEhEnableJUnit4MigrationSupport == True) and (contarLetrasEnableJUnit4MigrationSupport == 29)):
                                       if ('@EnableJUnit4MigrationSupport' == concatenarPalavras):
                                           achouAbreChaveEnableJUnit4MigrationSupport = False
                                           achouEnableJUnit4MigrationSupport          = True
                                           naoEhEnableJUnit4MigrationSupport          = False
                                           contEnableJUnit4MigrationSupport           += 1
                                           contarLetrasEnableJUnit4MigrationSupport   = 1
                                           concatenarPalavras                         = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasEnableJUnit4MigrationSupport = 1
                                       achouArrobaEnableJUnit4MigrationSupport  = True
                                       concatenarPalavras                       = ""
                                   
                                   contarLetrasEnableJUnit4MigrationSupport = 1
                                   concatenarPalavras                       += letra
                                   
                               elif (achouArrobaEnableJUnit4MigrationSupport == True):
                                     if (contarLetrasEnableJUnit4MigrationSupport == 29):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@EnableJUnit4MigrationSupport' == concatenarPalavras):
                                                 achouAbreChaveEnableJUnit4MigrationSupport = False
                                                 achouEnableJUnit4MigrationSupport          = True
                                                 naoEhEnableJUnit4MigrationSupport          = False
                                                 contEnableJUnit4MigrationSupport           += 1
                                                 contarLetrasEnableJUnit4MigrationSupport   = 0
                                                 concatenarPalavras                         = ""
                                             if (letra == "("):
                                                 concatenarPalavras                      = ""
                                                 flagEnableJUnit4MigrationSupport        = False
                                                 achouArrobaEnableJUnit4MigrationSupport = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasEnableJUnit4MigrationSupport += 1
                                             naoEhEnableJUnit4MigrationSupport        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras                      = ""
                                             flagEnableJUnit4MigrationSupport        = False
                                             achouArrobaEnableJUnit4MigrationSupport = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasEnableJUnit4MigrationSupport = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasEnableJUnit4MigrationSupport += 1
                                             naoEhEnableJUnit4MigrationSupport        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasEnableJUnit4MigrationSupport = True
                                   contarAspas                            += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas                            -= 2
                                   achouAspasEnableJUnit4MigrationSupport = False
                                   
                               if (achouAspasEnableJUnit4MigrationSupport != True):
                                   if (letra == ")"):
                                       flagEnableJUnit4MigrationSupport        = True 
                                       achouArrobaEnableJUnit4MigrationSupport = True
                                   elif (letra == "@"):
                                         concatenarPalavras                       = ""
                                         concatenarPalavras                       += letra
                                         contarLetrasEnableJUnit4MigrationSupport = 1
                                         flagEnableJUnit4MigrationSupport         = True
                                         achouArrobaEnableJUnit4MigrationSupport  = True
                                     
                       else:
                           if ((naoEhEnableJUnit4MigrationSupport == True) and (contarLetrasEnableJUnit4MigrationSupport == 29)):
                               if ('@EnableJUnit4MigrationSupport' == concatenarPalavras):
                                   concatenarPalavras                             = ""
                                   achouAbreChaveEnableJUnit4MigrationSupport     = False
                                   achouEnableJUnit4MigrationSupport              = True
                                   naoEhEnableJUnit4MigrationSupport              = False
                                   contEnableJUnit4MigrationSupport               += 1
                                   contarLetrasEnableJUnit4MigrationSupport       = 0
                                   barraPraComentarioEnableJUnit4MigrationSupport = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @EnableJUnit4MigrationSupport
                   if (barraPraComentarioEnableJUnit4MigrationSupport != True):
                       if ((len("@EnableJUnit4MigrationSupport") == contarLetrasEnableJUnit4MigrationSupport) or (len("@EnableJUnit4MigrationSupport") == contarLetrasEnableJUnit4MigrationSupport - 1)):
                           if ('@EnableJUnit4MigrationSupport' == concatenarPalavras):
                               concatenarPalavras                         = ""
                               contarLetrasEnableJUnit4MigrationSupport   = 0
                               achouAbreChaveEnableJUnit4MigrationSupport = False
                               achouEnableJUnit4MigrationSupport          = True
                               contEnableJUnit4MigrationSupport           += 1
             
       achouArrobaEnableJUnit4MigrationSupport        = False
       achouAspasEnableJUnit4MigrationSupport         = False
       barraPraComentarioEnableJUnit4MigrationSupport = False  

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@SuiteDisplayName' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioSuiteDisplayName = True
               elif (letra == '"'):
                     achouAspasSuiteDisplayName = True
               elif (letra == "@"):
                     flagSuiteDisplayName        = True
                     achouArrobaSuiteDisplayName = True
                     break
           
           if (barraPraComentarioSuiteDisplayName != True):
               if (achouAspasSuiteDisplayName != True):
                   contarLetrasSuiteDisplayName = 0
                   contarAspas                  = 0
                   naoEhSuiteDisplayName        = None
                   concatenarPalavras           = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagSuiteDisplayName == True) and (achouArrobaSuiteDisplayName == True)):
                               if (letra == "@"):
                                   if ((naoEhSuiteDisplayName == True) and (contarLetrasSuiteDisplayName == 17)):
                                       if ('@SuiteDisplayName' == concatenarPalavras):
                                           achouAbreChaveSuiteDisplayName = False
                                           achouSuiteDisplayName          = True
                                           naoEhSuiteDisplayName          = False
                                           contSuiteDisplayName           += 1
                                           contarLetrasSuiteDisplayName   = 1
                                           concatenarPalavras             = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasSuiteDisplayName = 1
                                       achouArrobaSuiteDisplayName  = True
                                       concatenarPalavras           = ""
                                       
                                   contarLetrasSuiteDisplayName = 1
                                   concatenarPalavras           += letra
                                   
                               elif (achouArrobaSuiteDisplayName == True):
                                     if (contarLetrasSuiteDisplayName == 17):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@SuiteDisplayName' == concatenarPalavras):
                                                 achouAbreChaveSuiteDisplayName = False
                                                 achouSuiteDisplayName          = True
                                                 naoEhSuiteDisplayName          = False
                                                 contSuiteDisplayName           += 1
                                                 contarLetrasSuiteDisplayName   = 0
                                                 concatenarPalavras             = ""
                                             if (letra == "("):
                                                 concatenarPalavras          = ""
                                                 flagSuiteDisplayName        = False
                                                 achouArrobaSuiteDisplayName = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasSuiteDisplayName += 1
                                             naoEhSuiteDisplayName        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras          = ""
                                             flagSuiteDisplayName        = False
                                             achouArrobaSuiteDisplayName = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasSuiteDisplayName = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasSuiteDisplayName += 1
                                             naoEhSuiteDisplayName        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasSuiteDisplayName = True
                                   contarAspas                += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas                -= 2
                                   achouAspasSuiteDisplayName = False
                                   
                               if (achouAspasSuiteDisplayName != True):
                                   if (letra == ")"):
                                       flagSuiteDisplayName        = True 
                                       achouArrobaSuiteDisplayName = True
                                   elif (letra == "@"):
                                         concatenarPalavras           = ""
                                         concatenarPalavras           += letra
                                         contarLetrasSuiteDisplayName = 1
                                         flagSuiteDisplayName         = True
                                         achouArrobaSuiteDisplayName  = True
                                     
                       else:
                           if ((naoEhSuiteDisplayName == True) and (contarLetrasSuiteDisplayName == 17)):
                               if ('@SuiteDisplayName' == concatenarPalavras):
                                   concatenarPalavras                 = ""
                                   achouAbreChaveSuiteDisplayName     = False
                                   achouSuiteDisplayName              = True
                                   naoEhSuiteDisplayName              = False
                                   contSuiteDisplayName               += 1
                                   contarLetrasSuiteDisplayName       = 0
                                   barraPraComentarioSuiteDisplayName = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @SuiteDisplayName
                   if (barraPraComentarioSuiteDisplayName != True):
                       if ((len("@SuiteDisplayName") == contarLetrasSuiteDisplayName) or (len("@SuiteDisplayName") == contarLetrasSuiteDisplayName - 1)):
                           if ('@SuiteDisplayName' == concatenarPalavras):
                               concatenarPalavras             = ""
                               contarLetrasSuiteDisplayName   = 0
                               achouAbreChaveSuiteDisplayName = False
                               achouSuiteDisplayName          = True
                               contSuiteDisplayName           += 1
             
       achouArrobaSuiteDisplayName        = False
       achouAspasSuiteDisplayName         = False
       barraPraComentarioSuiteDisplayName = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@UseTechnicalNames' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioUseTechnicalNames = True
               elif (letra == '"'):
                     achouAspasUseTechnicalNames = True
               elif (letra == "@"):
                     flagUseTechnicalNames        = True
                     achouArrobaUseTechnicalNames = True
                     break
           
           if (barraPraComentarioUseTechnicalNames != True):
               if (achouAspasUseTechnicalNames != True):
                   contarLetrasUseTechnicalNames = 0
                   contarAspas                   = 0
                   naoEhUseTechnicalNames        = None
                   contarAspas                   = 0
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagUseTechnicalNames == True) and (achouArrobaUseTechnicalNames == True)):
                               if (letra == "@"):
                                   if ((naoEhUseTechnicalNames == True) and (contarLetrasUseTechnicalNames == 18)):
                                       if ('@UseTechnicalNames' == concatenarPalavras):
                                           achouAbreChaveUseTechnicalNames = False
                                           achouUseTechnicalNames          = True
                                           naoEhUseTechnicalNames          = False
                                           contUseTechnicalNames           += 1
                                           contarLetrasUseTechnicalNames   = 1
                                           concatenarPalavras              = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasUseTechnicalNames = 1
                                       achouArrobaUseTechnicalNames  = True
                                       concatenarPalavras            = ""
                                       
                                   contarLetrasUseTechnicalNames = 1
                                   concatenarPalavras            += letra
                                   
                               elif (achouArrobaUseTechnicalNames == True):
                                     if (contarLetrasUseTechnicalNames == 18):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@UseTechnicalNames' == concatenarPalavras):
                                                 achouAbreChaveUseTechnicalNames = False
                                                 achouUseTechnicalNames          = True
                                                 naoEhUseTechnicalNames          = False
                                                 contUseTechnicalNames           += 1
                                                 contarLetrasUseTechnicalNames   = 0
                                                 concatenarPalavras              = ""
                                             if (letra == "("):
                                                 concatenarPalavras           = ""
                                                 flagUseTechnicalNames        = False
                                                 achouArrobaUseTechnicalNames = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasUseTechnicalNames += 1
                                             naoEhUseTechnicalNames        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras           = ""
                                             flagUseTechnicalNames        = False
                                             achouArrobaUseTechnicalNames = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasUseTechnicalNames = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasUseTechnicalNames += 1
                                             naoEhUseTechnicalNames        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasUseTechnicalNames = True
                                   contarAspas                 += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas                 -= 2
                                   achouAspasUseTechnicalNames = False
                                   
                               if (achouAspasUseTechnicalNames != True):
                                   if (letra == ")"):
                                       flagUseTechnicalNames        = True 
                                       achouArrobaUseTechnicalNames = True
                                   elif (letra == "@"):
                                         concatenarPalavras            = ""
                                         concatenarPalavras            += letra
                                         contarLetrasUseTechnicalNames = 1
                                         flagUseTechnicalNames         = True
                                         achouArrobaUseTechnicalNames  = True
                                     
                       else:
                           if ((naoEhUseTechnicalNames == True) and (contarLetrasUseTechnicalNames == 18)):
                               if ('@UseTechnicalNames' == concatenarPalavras):
                                   concatenarPalavras                  = ""
                                   achouAbreChaveUseTechnicalNames     = False
                                   achouUseTechnicalNames              = True
                                   naoEhUseTechnicalNames              = False
                                   contUseTechnicalNames               += 1
                                   contarLetrasUseTechnicalNames       = 0
                                   barraPraComentarioUseTechnicalNames = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @UseTechnicalNames
                   if (barraPraComentarioUseTechnicalNames != True):
                       if ((len("@UseTechnicalNames") == contarLetrasUseTechnicalNames) or (len("@UseTechnicalNames") == contarLetrasUseTechnicalNames - 1)):
                           if ('@UseTechnicalNames' == concatenarPalavras):
                               concatenarPalavras              = ""
                               contarLetrasUseTechnicalNames   = 0
                               achouAbreChaveUseTechnicalNames = False
                               achouUseTechnicalNames          = True
                               contUseTechnicalNames           += 1
             
       achouArrobaUseTechnicalNames        = False
       achouAspasUseTechnicalNames         = False
       barraPraComentarioUseTechnicalNames = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@SelectPackages' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioSelectPackages = True
               elif (letra == '"'):
                     achouAspasSelectPackages = True
               elif (letra == "@"):
                     flagSelectPackages        = True
                     achouArrobaSelectPackages = True
                     break
           
           if (barraPraComentarioSelectPackages != True):
               if (achouAspasSelectPackages != True):
                   contarLetrasSelectPackages = 0
                   contarAspas                = 0
                   naoEhSelectPackages        = None
                   concatenarPalavras         = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagSelectPackages == True) and (achouArrobaSelectPackages == True)):
                               if (letra == "@"):
                                   if ((naoEhSelectPackages == True) and (contarLetrasSelectPackages == 15)):
                                       if ('@SelectPackages' == concatenarPalavras):
                                           achouAbreChaveSelectPackages = False
                                           achouSelectPackages          = True
                                           naoEhSelectPackages          = False
                                           contSelectPackages           += 1
                                           contarLetrasSelectPackages   = 1
                                           concatenarPalavras           = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasSelectPackages = 1
                                       achouArrobaSelectPackages  = True
                                       concatenarPalavras         = ""
                                       
                                   contarLetrasSelectPackages = 1
                                   concatenarPalavras         += letra
                                   
                               elif (achouArrobaSelectPackages == True):
                                     if (contarLetrasSelectPackages == 15):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@SelectPackages' == concatenarPalavras):
                                                 achouAbreChaveSelectPackages = False
                                                 achouSelectPackages          = True
                                                 naoEhSelectPackages          = False
                                                 contSelectPackages           += 1
                                                 contarLetrasSelectPackages   = 0
                                                 concatenarPalavras           = ""
                                             if (letra == "("):
                                                 concatenarPalavras        = ""
                                                 flagSelectPackages        = False
                                                 achouArrobaSelectPackages = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasSelectPackages += 1
                                             naoEhSelectPackages        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras        = ""
                                             flagSelectPackages        = False
                                             achouArrobaSelectPackages = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasSelectPackages = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasSelectPackages += 1
                                             naoEhSelectPackages        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasSelectPackages = True
                                   contarAspas              += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas              -= 2
                                   achouAspasSelectPackages = False
                                   
                               if (achouAspasSelectPackages != True):
                                   if (letra == ")"):
                                       flagSelectPackages        = True 
                                       achouArrobaSelectPackages = True
                                   elif (letra == "@"):
                                         concatenarPalavras         = ""
                                         concatenarPalavras         += letra
                                         contarLetrasSelectPackages = 1
                                         flagSelectPackages         = True
                                         achouArrobaSelectPackages  = True
                                     
                       else:
                           if ((naoEhSelectPackages == True) and (contarLetrasSelectPackages == 15)):
                               if ('@SelectPackages' == concatenarPalavras):
                                   concatenarPalavras               = ""
                                   achouAbreChaveSelectPackages     = False
                                   achouSelectPackages              = True
                                   naoEhSelectPackages              = False
                                   contSelectPackages               += 1
                                   contarLetrasSelectPackages       = 0
                                   barraPraComentarioSelectPackages = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @SelectPackages
                   if (barraPraComentarioSelectPackages != True):
                       if ((len("@SelectPackages") == contarLetrasSelectPackages) or (len("@SelectPackages") == contarLetrasSelectPackages - 1)):
                           if ('@SelectPackages' == concatenarPalavras):
                               concatenarPalavras           = ""
                               contarLetrasSelectPackages   = 0
                               achouAbreChaveSelectPackages = False
                               achouSelectPackages          = True
                               contSelectPackages           += 1
             
       achouArrobaSelectPackages        = False
       achouAspasSelectPackages         = False
       barraPraComentarioSelectPackages = False 

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@JvmField' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioJvmField = True
               elif (letra == '"'):
                     achouAspasJvmField = True
               elif (letra == "@"):
                     flagJvmField        = True
                     achouArrobaJvmField = True
                     break
           
           if (barraPraComentarioJvmField != True):
               if (achouAspasJvmField != True):
                   contarLetrasJvmField = 0
                   contarAspas          = 0
                   naoEhJvmField        = None
                   concatenarPalavras   = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagJvmField == True) and (achouArrobaJvmField == True)):
                               if (letra == "@"):
                                   if ((naoEhJvmField == True) and (contarLetrasJvmField == 9)):
                                       if ('@JvmField' == concatenarPalavras):
                                           achouAbreChaveJvmField = False
                                           achouJvmField          = True
                                           naoEhJvmField          = False
                                           contJvmField           += 1
                                           contarLetrasJvmField   = 1
                                           concatenarPalavras     = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasJvmField = 1
                                       achouArrobaJvmField  = True
                                       concatenarPalavras   = ""
                                       
                                   contarLetrasJvmField = 1
                                   concatenarPalavras   += letra
                                   
                               elif (achouArrobaJvmField == True):
                                     if (contarLetrasJvmField == 9):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@JvmField' == concatenarPalavras):
                                                 achouAbreChaveJvmField = False
                                                 achouJvmField          = True
                                                 naoEhJvmField          = False
                                                 contJvmField           += 1
                                                 contarLetrasJvmField   = 0
                                                 concatenarPalavras     = ""
                                             if (letra == "("):
                                                 concatenarPalavras  = ""
                                                 flagJvmField        = False
                                                 achouArrobaJvmField = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasJvmField += 1
                                             naoEhJvmField        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras  = ""
                                             flagJvmField        = False
                                             achouArrobaJvmField = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasJvmField = 0
                                             
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasJvmField += 1
                                             naoEhJvmField        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasJvmField = True
                                   contarAspas        += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas        -= 2
                                   achouAspasJvmField = False
                                   
                               if (achouAspasJvmField != True):
                                   if (letra == ")"):
                                       flagJvmField        = True 
                                       achouArrobaJvmField = True
                                   elif (letra == "@"):
                                         concatenarPalavras   = ""
                                         concatenarPalavras   += letra
                                         contarLetrasJvmField = 1
                                         flagJvmField         = True
                                         achouArrobaJvmField  = True
                                     
                       else:
                           if ((naoEhJvmField == True) and (contarLetrasJvmField == 9)):
                               if ('@JvmField' == concatenarPalavras):
                                   concatenarPalavras         = ""
                                   achouAbreChaveJvmField     = False
                                   achouJvmField              = True
                                   naoEhJvmField              = False
                                   contJvmField               += 1
                                   contarLetrasJvmField       = 0
                                   barraPraComentarioJvmField = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @JvmField
                   if (barraPraComentarioJvmField != True):
                       if ((len("@JvmField") == contarLetrasJvmField) or (len("@JvmField") == contarLetrasJvmField - 1)):
                           if ('@JvmField' == concatenarPalavras):
                               concatenarPalavras     = ""
                               contarLetrasJvmField   = 0
                               achouAbreChaveJvmField = False
                               achouJvmField          = True
                               contJvmField           += 1
             
       achouArrobaJvmField        = False
       achouAspasJvmField         = False
       barraPraComentarioJvmField = False  

   datafile = open(f, errors="ignore")   
   for line in datafile:
       if '@interface' in line:
           for letra in line:
               if (letra == '/'):
                   barraPraComentarioInterface = True
               elif (letra == '"'):
                     achouAspasInterface = True
               elif (letra == "@"):
                     flagInterface        = True
                     achouArrobaInterface = True
                     break
           
           if (barraPraComentarioInterface != True):
               if (achouAspasInterface != True):
                   contarLetrasInterface = 0
                   contarAspas           = 0
                   naoEhInterface        = None
                   concatenarPalavras    = ""
                   for letra in line:
                       if (letra != "/"): 
                           if ((flagInterface == True) and (achouArrobaInterface == True)):
                               if (letra == "@"):
                                   if ((naoEhInterface == True) and (contarLetrasInterface == 10)):
                                       if ('@interface' == concatenarPalavras):
                                           achouAbreChaveInterface = False
                                           achouInterface          = True
                                           naoEhInterface          = False
                                           contInterface           += 1
                                           contarLetrasInterface   = 1
                                           concatenarPalavras      = ""
                                       else:
                                           concatenarPalavras = ""
                                   else:
                                       contarLetrasInterface = 1
                                       achouArrobaInterface  = True
                                       concatenarPalavras    = ""
                                       
                                   contarLetrasinterface = 1
                                   concatenarPalavras    += letra
                                   
                               elif (achouArrobaInterface == True):
                                     if (contarLetrasInterface == 10):
                                         if ((letra == "(")or(letra == " ")or
                                            (letra == "	")or(letra == ")")):
                                             if ('@interface' == concatenarPalavras):
                                                 achouAbreChaveInterface = False
                                                 achouInterface          = True
                                                 naoEhInterface          = False
                                                 contInterface           += 1
                                                 contarLetrasInterface   = 0
                                                 concatenarPalavras      = ""
                                             if (letra == "("):
                                                 concatenarPalavras   = ""
                                                 flagInterface        = False
                                                 achouArrobaInterface = False
                                                 
                                         else:
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasInterface += 1
                                             naoEhInterface        = False
                                     else:
                                         if (letra == "(")or(letra == ")"):
                                             concatenarPalavras   = ""
                                             flagInterface        = False
                                             achouArrobaInterface = False
                                         else:
                                             if ((letra == " ")or(letra == "	")):
                                                 contarLetrasInterface = 0
                                                 
                                             if (letra != " ")or(letra != " "):
                                                 concatenarPalavras += letra
                                                 
                                             contarLetrasInterface += 1
                                             naoEhInterface        = True
                                             
                           else:
                               if (letra == '"'):
                                   achouAspasInterface = True
                                   contarAspas         += 1
                                   
                               if (contarAspas == 2):
                                   contarAspas         -= 2
                                   achouAspasInterface = False
                                   
                               if (achouAspasInterface != True):
                                   if (letra == ")"):
                                       flagInterface        = True 
                                       achouArrobaInterface = True
                                   elif (letra == "@"):
                                         concatenarPalavras    = ""
                                         concatenarPalavras    += letra
                                         contarLetrasInterface = 1
                                         flagInterface         = True
                                         achouArrobaInterface  = True
                       else:
                           if ((naoEhInterface == True) and (contarLetrasInterface == 10)):
                               if ('@Interface' == concatenarPalavras):
                                   concatenarPalavras          = ""
                                   achouAbreChaveInterface     = False
                                   achouInterface              = True
                                   naoEhInterface              = False
                                   contInterface               += 1
                                   contarLetrasInterface       = 0
                                   barraPraComentarioInterface = True
                           else:
                               if (contarAspas == 0):
                                   break
                       
                   #Verifica a comparacao da igualdade da assinatura @Interface
                   if (barraPraComentarioInterface != True):
                       if ((len("@Interface") == contarLetrasInterface) or (len("@Interface") == contarLetrasInterface - 1)):
                           if ('@Interface' == concatenarPalavras):
                               concatenarPalavras      = ""
                               contarLetrasInterface   = 0
                               achouAbreChaveInterface = False
                               achouInterface          = True
                               contInterface           += 1
             
       achouArrobaInterface        = False
       achouAspasInterface         = False
       barraPraComentarioInterface = False       

   #Somatoria das variáveis
   totalContTest                          += contTest
   totalContAfterMethod                   += contAfterMethod
   totalContBeforeMethod                  += contBeforeMethod
   totalContAfter                         += contAfter 
   totalContBefore                        += contBefore   
   totalContParameterizedTest             += contParameterizedTest
   totalContRepeatedTest                  += contRepeatedTest
   totalContTestFactory                   += contTestFactory
   totalContTestTemplate                  += contTestTemplate
   totalContTestMethodOrder               += contTestMethodOrder
   totalContTestInstance                  += contTestInstance
   totalContDisplayName                   += contDisplayName
   totalContDisplayNameGeneration         += contDisplayNameGeneration
   totalContBeforeEach                    += contBeforeEach
   totalContAfterEach                     += contAfterEach
   totalContBeforeAll                     += contBeforeAll
   totalContAfterAll                      += contAfterAll
   totalContNested                        += contNested
   totalContTag                           += contTag
   totalContDisabled                      += contDisabled
   totalContTimeout                       += contTimeout
   totalContExtendWith                    += contExtendWith
   totalContRegisterExtension             += contRegisterExtension
   totalContTempDir                       += contTempDir
   totalContTestOnMac                     += contTestOnMac
   totalContOrder                         += contOrder
   totalContTarget                        += contTarget
   totalContRetention                     += contRetention
   totalContValueSource                   += contValueSource
   totalContEnabledOnOs                   += contEnabledOnOs
   totalContDisabledOnOs                  += contDisabledOnOs
   totalContEnabledOnJre                  += contEnabledOnJre
   totalContDisabledOnJre                 += contDisabledOnJre
   totalContEnabledIfSystemProperty       += contEnabledIfSystemProperty
   totalContDisabledIfSystemProperty      += contDisabledIfSystemProperty 
   totalContEnabledIfEnvironmentVariable  += contEnabledIfEnvironmentVariable
   totalContDisabledIfEnvironmentVariable += contDisabledIfEnvironmentVariable
   totalContEnabledIf                     += contEnabledIf
   totalContDisabledIf                    += contDisabledIf
   totalContFast                          += contFast
   totalContFastTest                      += contFastTest
   totalContNullSource                    += contNullSource
   totalContEmptySource                   += contEmptySource
   totalContNullAndEmptySource            += contNullAndEmptySource
   totalContEnumSource                    += contEnumSource
   totalContMethodSource                  += contMethodSource
   totalContCsvSource                     += contCsvSource
   totalContCsvFileSource                 += contCsvFileSource
   totalContArgumentsSource               += contArgumentsSource
   totalContAggregateWith                 += contAggregateWith
   totalContExecution                     += contExecution
   totalContResourceLock                  += contResourceLock
   totalContIgnore                        += contIgnore
   totalContCategory                      += contCategory
   totalContRunWith                       += contRunWith
   totalContRule                          += contRule
   totalContClassRule                     += contClassRule
   totalContEnableRuleMigrationSupport    += contEnableRuleMigrationSupport
   totalContEnableJUnit4MigrationSupport  += contEnableJUnit4MigrationSupport
   totalContSuiteDisplayName              += contSuiteDisplayName
   totalContUseTechnicalNames             += contUseTechnicalNames
   totalContSelectPackages                += contSelectPackages
   totalContJvmField                      += contJvmField
   totalContInterface                     += contInterface
   
   totalTestes    += (contTest+contAfterMethod+contBeforeMethod+contAfter+contBefore+contParameterizedTest+contRepeatedTest+contTestFactory+contTestTemplate+
                      contTestMethodOrder+contTestInstance+contDisplayName+contDisplayNameGeneration+contBeforeEach+contAfterEach+contBeforeAll+contAfterAll+
                      contNested+contTag+contDisabled+contTimeout+contExtendWith+contRegisterExtension+contTempDir+contTestOnMac+contOrder+contTarget+
                      contRetention+contValueSource+contEnabledOnOs+contDisabledOnOs+contEnabledOnJre+contDisabledOnJre+contEnabledIfSystemProperty+contDisabledIfSystemProperty+
                      contEnabledIfEnvironmentVariable+contDisabledIfEnvironmentVariable+contEnabledIf+contDisabledIf+contFast+contFastTest+contNullSource+
                      contEmptySource+contNullAndEmptySource+contEnumSource+contMethodSource+contCsvSource+contCsvFileSource+contArgumentsSource+contAggregateWith+
                      contExecution+contResourceLock+contIgnore+contCategory+contRunWith+contRule+contClassRule+contEnableRuleMigrationSupport+contEnableJUnit4MigrationSupport+
                      contSuiteDisplayName+contUseTechnicalNames+contSelectPackages+contJvmField+contInterface) 
   
   #Inicialização de variáveis
   contTest                  = 0
   contAfterMethod           = 0
   contBeforeMethod          = 0
   contAfter                 = 0    
   contBefore                = 0
   contParameterizedTest     = 0
   contRepeatedTest          = 0
   contTestFactory           = 0
   contTestTemplate          = 0
   contTestMethodOrder       = 0
   contTestInstance          = 0
   contDisplayName           = 0
   contDisplayNameGeneration = 0
   contBeforeEach            = 0
   contAfterEach             = 0
   contBeforeAll             = 0
   contAfterAll              = 0
   contNested                = 0
   contTag                   = 0
   contDisabled              = 0
   contTimeout               = 0
   contExtendWith            = 0
   contRegisterExtension     = 0
   contTempDir               = 0
   
   contTestOnMac                     = 0
   contOrder                         = 0
   contTarget                        = 0
   contRetention                     = 0
   contValueSource                   = 0
   contEnabledOnOs                   = 0
   contDisabledOnOs                  = 0
   contEnabledOnJre                  = 0
   contDisabledOnJre                 = 0
   contEnabledIfSystemProperty       = 0
   contDisabledIfSystemProperty      = 0
   contEnabledIfEnvironmentVariable  = 0
   contDisabledIfEnvironmentVariable = 0
   contEnabledIf                     = 0
   contDisabledIf                    = 0
   contFast                          = 0
   contFastTest                      = 0
   contNullSource                    = 0
   contEmptySource                   = 0
   contNullAndEmptySource            = 0
   contEnumSource                    = 0
   contMethodSource                  = 0
   contCsvSource                     = 0
   contCsvFileSource                 = 0
   contArgumentsSource               = 0
   contAggregateWith                 = 0
   contExecution                     = 0
   contResourceLock                  = 0
   contIgnore                        = 0
   contCategory                      = 0
   contRunWith                       = 0
   contRule                          = 0
   contClassRule                     = 0
   contEnableRuleMigrationSupport    = 0
   contEnableJUnit4MigrationSupport  = 0
   contSuiteDisplayName              = 0
   contUseTechnicalNames             = 0
   contSelectPackages                = 0
   contJvmField                      = 0
   contInterface                     = 0
   
#Impressão geral da análise

print(totalTestes)