const models = require('./models.json')
const fs = require('fs-extra')
const { resolve, basename } = require('path')
const { promisify } = require('util')
const exec = promisify(require('child_process').exec)
const tmp = require('tmp-promise')
const glob = require('glob-promise')

async function downloadZip(appName, url){
	const tmpFile = await tmp.file({ postfix : '.zip' })
	
	//download the file
	console.log('downloading', url)
	await exec(`curl ${url} -o ${tmpFile.path}`)
	
	const tmpDir = await tmp.dir({
		unsafeCleanup : true
	})
	//unzip it
	console.log('unzipping', url)
	await exec(`unzip ${tmpFile.path} -d ${tmpDir.path}`)

	//remove the tmp file
	tmpFile.cleanup()

	//move to the proper location
	const [sourceFolder] = await glob(resolve(tmpDir.path, '*/models'))
	await fs.move(sourceFolder, resolve(__dirname, '../magenta4live.amxd/code/public', appName, 'models'), {
		overwrite: true
	})

	tmpDir.cleanup()
}

async function main(){
	for (let modelName in models){
		const url = models[modelName].models
		await downloadZip(modelName, url)
	}
}

main()
