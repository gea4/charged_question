# Import file "question app"
qs = Framer.Importer.load("imported/question app@1x")
Utils.globalLayers(qs)

scrollingAnimation = new Animation
	layer: responses
	properties: 
		y: -1200
	time: 80
	
#scrollingAnimation.start()

responses.states.add
	down:
		y:300
		opacity: 0.0
responses.states.animationOptions =
	curve: "ease"
	time: 0.5
		
addResponse.on Events.Tap, ->
	responses.states.switch("down")
