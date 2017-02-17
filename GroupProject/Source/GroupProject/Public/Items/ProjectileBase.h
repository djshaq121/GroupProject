// Copyright LostGods

#pragma once

#include "GameFramework/Actor.h"
#include "ProjectileBase.generated.h"

UCLASS()
class GROUPPROJECT_API AProjectileBase : public AActor
{
	GENERATED_BODY()
	
public:	
	// Sets default values for this actor's properties
	AProjectileBase();

	// Called when the game starts or when spawned
	virtual void BeginPlay() override;
	
	// Called every frame
	virtual void Tick( float DeltaSeconds ) override;

	UFUNCTION()
	void OnHit(UPrimitiveComponent * HitComponent, AActor * OtherActor, UPrimitiveComponent * OtherComponent, FVector NormalImpulse, const FHitResult & Hit);

	void OnTimerExpire();

	void DealDamage(const FHitResult& Hit);
	
private:
	UPROPERTY(EditDefaultsOnly, meta = (AllowPirvateAccess = "true"))
	float BaseDamage;

	UPROPERTY(VisibleAnywhere,  meta = (AllowPirvateAccess = "true"))
	USkeletalMeshComponent* BulletMesh;

	UPROPERTY(VisibleAnywhere, meta = (AllowPirvateAccess = "true"))
	UProjectileMovementComponent* ProjectileMovement = nullptr;

	UPROPERTY(VisibleAnywhere, meta = (AllowPirvateAccess = "true"))
	USphereComponent* CollisonSphere;

	UPROPERTY(EditDefaultsOnly, Category = "Setup")
		float DestroyDelay = 10.f;

	UPROPERTY(EditDefaultsOnly, Category = "Setup")
		float ProjectileDamage = 20.f;
	
};
