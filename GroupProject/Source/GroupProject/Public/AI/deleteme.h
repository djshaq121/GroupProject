// Copyright 

#pragma once

#include "GameFramework/Actor.h"
#include "deleteme.generated.h"

UCLASS()
class GROUPPROJECT_API Adeleteme : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	Adeleteme();

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;
	
	// Called every frame
	virtual void Tick( float DeltaSeconds ) override;

	
	
};
