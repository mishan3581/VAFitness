chcp 65001
"C:\Program Files (x86)\1cv8\8.3.24.1368\bin\1cv8c" /N"Админ" /TestManager /Execute "C:\VA_test\vanessa-automation\vanessa-automation.epf" /IBConnectionString "Srvr=""DESKTOP-BIF25NH"";Ref=""VAFitness"";" /C"StartFeaturePlayer;QuietInstallVanessaExt;VAParams=C:\Users\Алексей\Desktop\VAParams\VAParams.json"
allure generate --clean "C:\Users\Алексей\Desktop\Allure" && allure open